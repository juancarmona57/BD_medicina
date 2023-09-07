visitas = []

def validar_cedula(cedula):
    global visitas
    # Comprueba que la cédula tenga exactamente 10 dígitos y sea única.
    return len(cedula) == 10 and cedula not in [visita['cedula'] for visita in visitas]

def registrar_datos_vitales(cedula_paciente, presion, temperatura, pulso, oxigeno):
    global visitas

    if not validar_cedula(cedula_paciente):
        print("Número de cédula inválido o ya está registrado.")
        return

    visita = {
        "cedula": cedula_paciente, 
        "presion": presion, 
        "temperatura": temperatura, 
        "pulso": pulso, 
        "oxigeno": oxigeno, 
        "medicamento": None, 
        "orden": None,
        "observaciones": None, 
        "prueba": None, 
        "resultado": None,
        "recordatorio_fecha": None, 
        "recordatorio_motivo": None
    }

    visitas.append(visita)
    print("Datos vitales registrados exitosamente.")

def registrar_medicamentos(cedula_paciente, medicamento, orden, observaciones):
    global visitas

    for visita in visitas:
        if visita['cedula'] == cedula_paciente:
            visita['medicamento'] = medicamento
            visita['orden'] = orden
            visita['observaciones'] = observaciones
            break

    print("Medicamentos registrados exitosamente.")

def registrar_pruebas(cedula_paciente, prueba, resultado):
    global visitas

    for visita in visitas:
        if visita['cedula'] == cedula_paciente:
            visita['prueba'] = prueba
            visita['resultado'] = resultado
            break

    print("Pruebas registradas exitosamente.")

def programar_recordatorio(cedula_paciente, fecha, motivo):
    global visitas

    for visita in visitas:
        if visita['cedula'] == cedula_paciente:
            visita['recordatorio_fecha'] = fecha
            visita['recordatorio_motivo'] = motivo
            break

    print("Recordatorio programado exitosamente.")

def menu_enfermera():
    global visitas

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
            registrar_datos_vitales(cedula, presion, temperatura, pulso, oxigeno)
        elif opcion == "2":
            cedula = input("Ingrese cédula del paciente: ")
            medicamento = input("Ingrese nombre del medicamento: ")
            orden = input("Ingrese orden asociada: ")
            observaciones = input("Ingrese observaciones (si las hay, sino dejar en blanco): ")
            registrar_medicamentos(cedula, medicamento, orden, observaciones)
        elif opcion == "3":
            cedula = input("Ingrese cédula del paciente: ")
            prueba = input("Ingrese nombre de la prueba: ")
            resultado = input("Ingrese resultado de la prueba: ")
            registrar_pruebas(cedula, prueba, resultado)
        elif opcion == "4":
            cedula = input("Ingrese cédula del paciente: ")
            fecha = input("Ingrese fecha del recordatorio (DD/MM/YYYY): ")
            motivo = input("Ingrese motivo del recordatorio: ")
            programar_recordatorio(cedula, fecha, motivo)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

