import re
from datetime import datetime
import pandas as pd

def crear_base_datos():
    columns = [
        "nombre", "cedula", "correo", "telefono", "fecha_nacimiento",
        "direccion", "rol", "usuario", "contraseña"
    ]
    return pd.DataFrame(columns=columns)

def guardar_csv(df, archivo='base_datos.csv'):
    df.to_csv(archivo, index=False)

def cargar_csv(archivo='base_datos.csv'):
    try:
        return pd.read_csv(archivo)
    except FileNotFoundError:
        return crear_base_datos()

class Persona:
    def __init__(self):
        self.base_datos = cargar_csv()

    def validar_correo(self, correo):
        return re.match(r'^[\w\.-]+@[\w\.-]+$', correo)

    def validar_telefono(self, telefono):
        return re.match(r'^\d{10}$', telefono)

    def validar_cedula(self, cedula):
        return re.match(r'^\d{10}$', cedula) and cedula not in self.base_datos['cedula'].values

    def validar_fecha(self, fecha):
        try:
            datetime.strptime(fecha, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validar_contraseña(self, contraseña):
        return (any(c.isupper() for c in contraseña) and
                any(c.isdigit() for c in contraseña) and
                any(c in '!@#$%^&*()_-+={}[]|\:;"<>,.?/~' for c in contraseña) and
                len(contraseña) >= 8)

    def registrar_persona(self):
        nombre = input("Nombre completo: ")
        while True:
            cedula = input("Número de cédula: ")
            if not self.validar_cedula(cedula):
                print("Verificar cédula número de caracteres o cédula ya registrada.")
            else:
                break

        correo = input("Correo electrónico: ")
        while not self.validar_correo(correo):
            correo = input("Correo electrónico inválido. Ingrese un correo válido: ")

        telefono = input("Número de teléfono: ")
        while not self.validar_telefono(telefono):
            telefono = input("Número de teléfono inválido. Ingrese un número de 10 dígitos: ")

        

        fecha_nacimiento = input("Fecha de nacimiento (DD/MM/YYYY): ")
        while not self.validar_fecha(fecha_nacimiento):
            fecha_nacimiento = input("Fecha de nacimiento inválida. Ingrese una fecha en formato DD/MM/YYYY: ")

        direccion = input("Dirección (máximo 30 caracteres): ")[:30]

        rol = input("Rol: ")

        usuario = input("Nombre de usuario: ")

        contraseña = input("Contraseña: ")
        while not self.validar_contraseña(contraseña):
            contraseña = input("Contraseña inválida. Debe incluir al menos una mayúscula, un número, un carácter especial y tener al menos 8 caracteres: ")

        nueva_persona = {
            "nombre": nombre, "cedula": cedula, "correo": correo, "telefono": telefono,
            "fecha_nacimiento": fecha_nacimiento, "direccion": direccion, "rol": rol,
            "usuario": usuario, "contraseña": contraseña
        }
        # Agregar la nueva persona al DataFrame usando loc
        self.base_datos.loc[len(self.base_datos)] = nueva_persona
        print("¡Persona registrada exitosamente!")

    def eliminar_persona(self):
        cedula_eliminar = input("Ingrese la cédula de la persona que desea eliminar: ")
        self.base_datos = self.base_datos[self.base_datos['cedula'] != cedula_eliminar]
        print("¡Persona eliminada exitosamente!")

    def mostrar_personas(self):
        print("Personas registradas:")
        for index, persona in self.base_datos.iterrows():
            print(f"Nombre: {persona['nombre']}")
            print(f"Cédula: {persona['cedula']}")
            print(f"Correo: {persona['correo']}")
            print(f"Teléfono: {persona['telefono']}")
            print(f"Fecha de Nacimiento: {persona['fecha_nacimiento']}")
            print(f"Dirección: {persona['direccion']}")
            print(f"Rol: {persona['rol']}")
            print(f"Usuario: {persona['usuario']}")
            print("----------------------")

def main():
    persona_handler = Persona()

    while True:
        print("Registro de Personas")
        print("1. Registrar nueva persona")
        print("2. Mostrar todas las personas registradas")
        print("3. Eliminar persona")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            persona_handler.registrar_persona()
        elif opcion == "2":
            persona_handler.mostrar_personas()
        elif opcion == "3":
            persona_handler.eliminar_persona()
        elif opcion == "4":
            guardar_csv(persona_handler.base_datos)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    main()
