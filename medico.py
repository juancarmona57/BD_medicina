# Listas de almacenamiento
historias_clinicas = []
ordenes_medicamentos = []
ordenes_procedimientos = []

def registrar_historia_clinica():
    cedula_paciente = input("Ingrese cédula del paciente: ")
    historia = input("Ingrese la historia clínica: ")
    historias_clinicas.append({
        "cedula_paciente": cedula_paciente,
        "historia": historia
    })
    print("Historia clínica registrada exitosamente.")

def prescribir_medicamento():
    global ordenes_medicamentos

    cedula_paciente = input("Ingrese cédula del paciente: ")
    cedula_medico = input("Ingrese su cédula: ")
    fecha = input("Fecha de prescripción (DD/MM/YYYY): ")

    medicamentos = []
    num_medicamentos = int(input("¿Cuántos medicamentos va a prescribir? "))
    for _ in range(num_medicamentos):
        nombre = input("Nombre del medicamento: ")
        dosis = input("Dosis: ")
        duracion = input("Duración: ")
        medicamentos.append({
            "nombre": nombre,
            "dosis": dosis,
            "duracion": duracion
        })

    registrar_orden_medicamento(cedula_paciente, cedula_medico, fecha, medicamentos)

def solicitar_procedimiento():
    global ordenes_procedimientos

    cedula_paciente = input("Ingrese cédula del paciente: ")
    cedula_medico = input("Ingrese su cédula: ")
    fecha = input("Fecha de solicitud (DD/MM/YYYY): ")

    procedimientos = []
    num_procedimientos = int(input("¿Cuántos procedimientos va a solicitar? "))
    for _ in range(num_procedimientos):
        nombre = input("Nombre del procedimiento: ")
        veces = int(input("Número de veces que se repetirá: "))
        frecuencia = input("Frecuencia de repetición: ")
        procedimientos.append({
            "nombre": nombre,
            "veces": veces,
            "frecuencia": frecuencia
        })

    registrar_orden_procedimiento(cedula_paciente, cedula_medico, fecha, procedimientos)

def registrar_orden_medicamento(cedula_paciente, cedula_medico, fecha, medicamentos):
    global ordenes_medicamentos

    numero_orden = len(ordenes_medicamentos) + 1
    orden = {
        "numero_orden": numero_orden,
        "cedula_paciente": cedula_paciente,
        "cedula_medico": cedula_medico,
        "fecha_creacion": fecha,
        "medicamentos": medicamentos
    }
    ordenes_medicamentos.append(orden)
    print("Orden de medicamento registrada exitosamente.")

def registrar_orden_procedimiento(cedula_paciente, cedula_medico, fecha, procedimientos):
    global ordenes_procedimientos

    numero_orden = len(ordenes_procedimientos) + 1
    orden = {
        "numero_orden": numero_orden,
        "cedula_paciente": cedula_paciente,
        "cedula_medico": cedula_medico,
        "fecha_creacion": fecha,
        "procedimientos": procedimientos
    }
    ordenes_procedimientos.append(orden)
    print("Orden de procedimiento registrada exitosamente.")

def menu_medico():
    global personas
    while True:
        print("Sistema Médico")
        print("1. Registrar historia clínica")
        print("2. Prescribir medicamentos")
        print("3. Solicitar procedimientos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_historia_clinica()
        elif opcion == "2":
            prescribir_medicamento()
        elif opcion == "3":
            solicitar_procedimiento()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

