from datetime import datetime

def validar_correo(correo):
    return correo == "" or ('@' in correo)

def registrar_paciente():
    nombre = input("Nombre completo del paciente: ")
    cedula = input("Número de cédula (10 caracteres): ")
    while len(cedula) != 10:
        cedula = input("Número de cédula inválido. Ingrese un número de 10 dígitos: ")

    correo = input("Correo electrónico (dejar en blanco si no tiene): ")
    while not validar_correo(correo):
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

    return nuevo_paciente

def menu_administrativo():
    pacientes = []

    while True:
        print("Sistema Administrativo")
        print("1. Registrar paciente")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            paciente = registrar_paciente()
            pacientes.append(paciente)
            print("¡Paciente registrado exitosamente!")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")