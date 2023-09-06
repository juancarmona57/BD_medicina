import pandas as pd
from datetime import datetime

class RegistroPacientes:
    def __init__(self):
        self.base_datos = self.cargar_csv()

    def cargar_csv(self, archivo='pacientes.csv'): 
        try:
            return pd.read_csv(archivo)
        except FileNotFoundError:
            return self.crear_base_datos()

    def crear_base_datos(self):
        columns = [
            "nombre", "cedula", "correo", "telefono", "fecha_nacimiento",
            "direccion", "genero"
        ]
        return pd.DataFrame(columns=columns)

    def validar_correo(self, correo):
        return correo == "" or ('@' in correo)

    def registrar_paciente(self):
        nombre = input("Nombre completo del paciente: ")
        cedula = input("Número de cédula (10 caracteres): ")
        while len(cedula) != 10:
            cedula = input("Número de cédula inválido. Ingrese un número de 10 dígitos: ")

        correo = input("Correo electrónico (dejar en blanco si no tiene): ")
        while not self.validar_correo(correo):
            correo = input("El correo debe incluir el dominio @ (o deje en blanco si no tiene): ")

        telefono = input("Número de teléfono: ")
        fecha_nacimiento = input("Fecha de nacimiento (DD/MM/YYYY): ")

        genero = input("Género (F para femenino, M para masculino, O para otro): ")
        genero = genero.upper()
        while genero not in ['F', 'M', 'O']:
            genero = input("Género inválido. Ingrese F para femenino, M para masculino, O para otro: ")
            genero = genero.upper()

        direccion = input("Dirección: ")

        # Información de contacto de emergencia
        nombre_contacto_emergencia = input("Nombre del contacto de emergencia (Separe nombres y apellidos): ")
        relacion_paciente = input("Relación con el paciente: ")
        telefono_emergencia = input("Número de teléfono de emergencia (máximo 10 dígitos): ")
        while len(telefono_emergencia) != 10 or not telefono_emergencia.isdigit():
            telefono_emergencia = input("Número de teléfono inválido. Ingrese un número de 10 dígitos: ")

        # Información de seguro médico
        nombre_compania_seguros = input("Nombre de la compañía de seguros: ")
        numero_poliza = input("Número de póliza del seguro médico del paciente: ")
        estado_poliza = input("Estado de la póliza (activo/inactivo): ").lower()
        while estado_poliza not in ['activo', 'inactivo']:
            estado_poliza = input("Estado de la póliza inválido. Ingrese 'activo' o 'inactivo': ").lower()

        # Actualizar diccionario de paciente con la nueva información
        nuevo_paciente = {
            "nombre": nombre, 
            "cedula": cedula, 
            "correo": correo, 
            "telefono": telefono,
            "fecha_nacimiento": fecha_nacimiento, 
            "genero": genero, 
            "direccion": direccion,
            "nombre_contacto_emergencia": nombre_contacto_emergencia,
            "relacion_paciente": relacion_paciente,
            "telefono_emergencia": telefono_emergencia,
            "nombre_compania_seguros": nombre_compania_seguros,
            "numero_poliza": numero_poliza,
            "estado_poliza": estado_poliza
        }

        self.base_datos.loc[len(self.base_datos)] = nuevo_paciente
        self.guardar_csv()  # Guardar la base de datos en el archivo CSV después de registrar un paciente
        print("¡Paciente registrado exitosamente!")

    def guardar_csv(self, archivo='pacientes.csv'):
        self.base_datos.to_csv(archivo, index=False)

class Factura:
    def __init__(self, base_datos_pacientes):
        self.base_datos_pacientes = base_datos_pacientes
        self.base_datos_facturas = self.cargar_csv_facturas()
        self.total_copagos_anuales = {}  # Para almacenar la suma de los copagos de cada paciente en el año

    def cargar_csv_facturas(self, archivo='base_datos_facturas.csv'):
        try:
            return pd.read_csv(archivo)
        except FileNotFoundError:
            return self.crear_base_datos_facturas()

    def crear_base_datos_facturas(self):
        columns = [
            "nombre_paciente", "edad", "cedula", "nombre_medico", "nombre_compania_seguro",
            "numero_poliza", "vigencia_poliza", "diagnostico", "total_cobro"
        ]
        return pd.DataFrame(columns=columns)

    def generar_factura(self, cedula_paciente, nombre_medico, diagnostico, medicamentos=[], procedimientos=[], examenes=[]):
        paciente = self.base_datos_pacientes[self.base_datos_pacientes['cedula'] == cedula_paciente].iloc[0]

        # Calcular edad del paciente
        fecha_nacimiento = datetime.strptime(paciente['fecha_nacimiento'], '%d/%m/%Y')
        edad = datetime.now().year - fecha_nacimiento.year - ((datetime.now().month, datetime.now().day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        # Calcular total del cobro
        total_cobro = sum([med['costo'] for med in medicamentos])  # Suma de los costos de los medicamentos
        if paciente['estado_poliza'] == 'activo':
            copago = 50000
            self.total_copagos_anuales[cedula_paciente] = self.total_copagos_anuales.get(cedula_paciente, 0) + copago
            if self.total_copagos_anuales[cedula_paciente] > 1000000:  # Si ha pagado más de un millón en copagos en el año
                copago = 0
            total_cobro += copago
        else:
            total_cobro += 200000  # Costo base cuando la póliza está inactiva o no tiene

        # Crear la factura
        factura = {
            "nombre_paciente": paciente['nombre'],
            "edad": edad,
            "cedula": cedula_paciente,
            "nombre_medico": nombre_medico,
            "nombre_compania_seguro": paciente['nombre_compania_seguros'],
            "numero_poliza": paciente['numero_poliza'],
            "vigencia_poliza": "Activa" if paciente['estado_poliza'] == 'activo' else "Inactiva",
            "diagnostico": diagnostico,
            "total_cobro": total_cobro
        }
        
        self.base_datos_facturas.loc[len(self.base_datos_facturas)] = factura
        self.guardar_csv_facturas()  # Guardar la base de facturas en el archivo CSV después de generar una factura
        print("¡Factura generada exitosamente!")
        # Aquí podrías agregar más lógica para imprimir la factura o guardarla en un archivo, si es necesario.

    def guardar_csv_facturas(self, archivo='base_datos_facturas.csv'):
        self.base_datos_facturas.to_csv(archivo, index=False)

    def mostrar_factura(self, cedula_paciente):
        factura = self.base_datos_facturas[self.base_datos_facturas['cedula'] == cedula_paciente].iloc[0]
        # Aquí podrías agregar lógica para imprimir la factura en un formato específico o mostrarla en pantalla.

def main():
    registro_handler = RegistroPacientes()
    factura_handler = Factura(registro_handler.base_datos)

    while True:
        print("Menú Principal")
        print("1. Registrar nuevo paciente")
        print("2. Generar factura")
        print("3. Mostrar factura")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registro_handler.registrar_paciente()
        elif opcion == "2":
            cedula_paciente = input("Ingrese la cédula del paciente: ")
            nombre_medico = input("Ingrese el nombre del médico tratante: ")
            diagnostico = input("Ingrese el diagnóstico: ")
            # Aquí puedes añadir lógica para ingresar medicamentos, procedimientos y exámenes si es necesario
            factura_handler.generar_factura(cedula_paciente, nombre_medico, diagnostico)
        elif opcion == "3":
            cedula_paciente = input("Ingrese la cédula del paciente para mostrar su factura: ")
            factura_handler.mostrar_factura(cedula_paciente)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
