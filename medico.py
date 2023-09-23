import recursos_humanos as rh
import personal_administrativo as pa
from controladores import registrar_historia_clinica_controlador  # Importamos el controlador


class Medico:
    ordenes_db = []
    ordenes_medicamento_db = []
    ordenes_procedimiento_db = []

    @classmethod
    def obtener_numero_orden(cls):
        if cls.ordenes_db:
            return str(int(cls.ordenes_db[-1]["numero_orden"]) + 1).zfill(6)
        return "000001"

    @classmethod
    def medico_existe(cls, cedula):
        for persona in rh.personas:
            if persona['cedula'] == cedula and persona['rol'] == 'medico':
                return True
        return False

    @classmethod
    def paciente_existe(cls, cedula):
        try:
            return cedula in [pacientes['cedula'] for pacientes in pa.pacientes]
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return False

    @classmethod
    def desplegar_menu_acciones():
        opciones = ["Medicamentos", "Procedimientos", "Ayuda Diagnóstica", "Salir"]
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        eleccion = int(input("Elige una opción: "))
        return opciones[eleccion - 1]

    @classmethod
    def desplegar_menu_acciones():
        print("\n--- Acciones ---")
        print("1. Medicamentos")
        print("2. Procedimientos")
        print("3. Ayuda Diagnóstica")
        print("4. Salir")

        opciones = ["Medicamentos", "Procedimientos", "Ayuda Diagnóstica", "Salir"]
        eleccion = input("Seleccione una opción: ")

        while eleccion not in ["1", "2", "3", "4"]:
            print("Opción inválida. Por favor, intente de nuevo.")
            eleccion = input("Seleccione una opción: ")

        return opciones[int(eleccion) - 1]

    @classmethod
    def registrar_historia_clinica(cls):
        print("----- Registro de Historia Clínica -----")
        cedula_paciente = input("Cédula del paciente: ")
        
        while not pa.paciente_existe(cedula_paciente):  # Utilizamos la función paciente_existe de personal_administrativo
            print("La cédula ingresada no corresponde a un paciente registrado.")
            cedula_paciente = input("Cédula del paciente: ")

        fecha_atencion = input("Fecha de atención (DD/MM/YYYY): ")
        cedula_medico = input("Cédula del médico que lo atendió (10 dígitos máx.): ")
        
        while len(cedula_medico) > 10 or not cls.medico_existe(cedula_medico):
            print("Verifique que la cédula tenga 10 dígitos y corresponda a un médico registrado.")
            cedula_medico = input("Cédula del médico que lo atendió (10 dígitos máx.): ")

        motivo_consulta = input("Motivo de la consulta: ")
        sintomatologia = input("Sintomatología: ")
        diagnostico = input("Diagnóstico: ")

        registro_consulta = {
            "cedula_medico": cedula_medico,
            "motivo_consulta": motivo_consulta,
            "sintomatologia": sintomatologia,
            "diagnostico": diagnostico
        }

        # Usamos el controlador para registrar la historia clínica
        resultado = registrar_historia_clinica_controlador(cedula_paciente, registro_consulta)
        print(resultado['mensaje'])

        numero_orden_actual = cls.obtener_numero_orden()

        while True:
            accion = cls.desplegar_menu_acciones()

            if accion == "Salir":
                break

            if accion == "Medicamentos":
                numero_item = 1  
                while True:
                    nombre_med = input("Nombre del medicamento: ")
                    dosis = input("Dosis: ")
                    duracion = input("Duración del tratamiento: ")
                    costo = input("Costo del medicamento: ")

                    orden_medicamento = {
                        "numero_orden": numero_orden_actual,
                        "numero_item": numero_item,
                        "nombre_medicamento": nombre_med,
                        "dosis": dosis,
                        "duracion": duracion,
                        "costo": costo
                    }

                    cls.ordenes_medicamento_db.append(orden_medicamento)
                    respuesta = input("¿Desea agregar otro medicamento a la misma orden? (S/N): ").upper()
                    if respuesta == "N":
                        break
                    numero_item += 1

            elif accion == "Procedimientos":
                numero_item = 1  
                while True:
                    nombre_proc = input("Nombre del procedimiento: ")
                    repite = input("Número de veces que se repite: ")
                    frecuencia = input("Frecuencia con la que se repite: ")
                    costo = input("Costo del procedimiento: ")
                    requiere_especialista = input("Requiere asistencia de especialista (S/N): ").upper() == "S"

                    orden_procedimiento = {
                        "numero_orden": numero_orden_actual,
                        "numero_item": numero_item,
                        "nombre_procedimiento": nombre_proc,
                        "repeticiones": repite,
                        "frecuencia": frecuencia,
                        "costo": costo,
                        "asistencia_especialista": requiere_especialista
                    }

                    cls.ordenes_procedimiento_db.append(orden_procedimiento)
                    respuesta = input("¿Desea agregar otro procedimiento a la misma orden? (S/N): ").upper()
                    if respuesta == "N":
                        break
                    numero_item += 1

            orden_data = {
                "numero_orden": numero_orden_actual,
                "cedula_paciente": cedula_paciente,
                "cedula_medico": cedula_medico,
                "fecha_creacion": fecha_atencion,
                "tipo_orden": accion.lower()
            }
            cls.ordenes_db.append(orden_data)
            numero_orden_actual = cls.obtener_numero_orden()  

        print("Historial clínico actualizado con éxito!")

    @classmethod
    def menu_medico(cls):
        while True:
            print("\n--- Menú Médico ---")
            print("1. Registrar Historia Clínica")
            print("2. Salir")
            eleccion = input("Seleccione una opción: ")

            if eleccion == "1":
                cls.registrar_historia_clinica()
            elif eleccion == "2":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")



