import pandas as pd

def cargar_csv(archivo):
    try:
        return pd.read_csv(archivo)
    except FileNotFoundError:
        return crear_base_datos_visitas()

def crear_base_datos_visitas():
    columns = [
        "cedula", "presion", "temperatura", "pulso", "oxigeno",
        "medicamento", "orden", "observaciones", "prueba", "resultado", 
        "recordatorio_fecha", "recordatorio_motivo"
    ]
    return pd.DataFrame(columns=columns)

class Enfermera:
    def __init__(self):
        self.base_datos_pacientes = cargar_csv('base_datos_pacientes.csv')
        self.base_datos_visitas = cargar_csv('base_datos_visitas.csv')

    def validar_cedula(self, cedula):
        # Comprueba que la cédula tenga exactamente 10 dígitos y sea única.
        return len(cedula) == 10 and cedula not in self.base_datos_visitas['cedula'].values

    def registrar_datos_vitales(self, cedula_paciente, presion, temperatura, pulso, oxigeno):
        if not self.validar_cedula(cedula_paciente):
            print("Número de cédula inválido o ya está registrado.")
            return

        visita = {
            "cedula": cedula_paciente, "presion": presion, "temperatura": temperatura, 
            "pulso": pulso, "oxigeno": oxigeno, "medicamento": None, "orden": None,
            "observaciones": None, "prueba": None, "resultado": None,
            "recordatorio_fecha": None, "recordatorio_motivo": None
        }
        self.base_datos_visitas.loc[len(self.base_datos_visitas)] = visita
        print("Datos vitales registrados exitosamente.")

    def registrar_medicamentos(self, cedula_paciente, medicamento, orden, observaciones):
        self.base_datos_visitas.loc[self.base_datos_visitas['cedula'] == cedula_paciente, ['medicamento', 'orden', 'observaciones']] = medicamento, orden, observaciones
        print("Medicamentos registrados exitosamente.")

    def registrar_pruebas(self, cedula_paciente, prueba, resultado):
        self.base_datos_visitas.loc[self.base_datos_visitas['cedula'] == cedula_paciente, ['prueba', 'resultado']] = prueba, resultado
        print("Pruebas registradas exitosamente.")

    def programar_recordatorio(self, cedula_paciente, fecha, motivo):
        self.base_datos_visitas.loc[self.base_datos_visitas['cedula'] == cedula_paciente, ['recordatorio_fecha', 'recordatorio_motivo']] = fecha, motivo
        print("Recordatorio programado exitosamente.")

    def guardar_csv(self, archivo='base_datos_visitas.csv'):
        self.base_datos_visitas.to_csv(archivo, index=False)

def main():
    enfermera_handler = Enfermera()

    while True:
        print("Sistema de Enfermeras")
        print("1. Registrar datos vitales")
        print("2. Registrar medicamentos")
        print("3. Registrar pruebas")
        print("4. Programar recordatorio")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("Ingrese cédula del paciente: ")
            presion = input("Ingrese presión arterial: ")
            temperatura = input("Ingrese temperatura: ")
            pulso = input("Ingrese pulso: ")
            oxigeno = input("Ingrese nivel de oxígeno en sangre: ")
            enfermera_handler.registrar_datos_vitales(cedula, presion, temperatura, pulso, oxigeno)
        elif opcion == "2":
            cedula = input("Ingrese cédula del paciente: ")
            medicamento = input("Ingrese nombre del medicamento: ")
            orden = input("Ingrese orden asociada: ")
            observaciones = input("Ingrese observaciones (si las hay, sino dejar en blanco): ")
            enfermera_handler.registrar_medicamentos(cedula, medicamento, orden, observaciones)
        elif opcion == "3":
            cedula = input("Ingrese cédula del paciente: ")
            prueba = input("Ingrese nombre de la prueba: ")
            resultado = input("Ingrese resultado de la prueba: ")
            enfermera_handler.registrar_pruebas(cedula, prueba, resultado)
        elif opcion == "4":
            cedula = input("Ingrese cédula del paciente: ")
            fecha = input("Ingrese fecha del recordatorio (DD/MM/YYYY): ")
            motivo = input("Ingrese motivo del recordatorio: ")
            enfermera_handler.programar_recordatorio(cedula, fecha, motivo)
        elif opcion == "5":
            enfermera_handler.guardar_csv()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
