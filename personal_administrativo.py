import re
from datetime import datetime
import medico as me

COPAGO = 50000
LIMITE_COPAGO = 1000000

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def registrar_paciente():
    print("----- Datos Personales del Paciente -----")
    numero_identificacion = input("Número de Identificación: ")
    nombre_completo = input("Nombre completo: ")
    cedula = input("Cédula (10 caracteres): ")
    while len(cedula) != 10 or not cedula.isdigit():
        print("Cédula inválida. Debe tener 10 caracteres numéricos.")
        cedula = input("Cédula (10 caracteres): ")

    fecha_nacimiento = input("Fecha de nacimiento (DD/MM/YYYY): ")
    genero = input("Género (masculino, femenino, otro): ")
    direccion = input("Dirección: ")
    numero_telefono = input("Número de teléfono: ")
    correo_electronico = input("Correo electrónico (opcional): ")

    print("----- Información de Contacto de Emergencia -----")
    nombre_contacto_emergencia = input("Nombre del contacto de emergencia: ")
    relacion_con_paciente = input("Relación con el paciente: ")
    numero_telefono_emergencia = input("Número de teléfono de emergencia (Máximo 10 dígitos): ")
    while len(numero_telefono_emergencia) > 10 or not numero_telefono_emergencia.isdigit():
        print("Número inválido. Debe tener un máximo de 10 dígitos numéricos.")
        numero_telefono_emergencia = input("Número de teléfono de emergencia (Máximo 10 dígitos): ")

    print("----- Información de Seguro Médico -----")
    nombre_compania_seguros = input("Nombre de la compañía de seguros: ")
    numero_poliza = input("Número de póliza: ")
    estado_poliza_str = input("Estado de la póliza (activo/inactivo): ").lower()
    estado_poliza = estado_poliza_str == "activo"

    paciente = {
        "numero_identificacion": numero_identificacion,
        "nombre": nombre_completo,
        "cedula": cedula,
        "fecha_nacimiento": fecha_nacimiento,
        "genero": genero,
        "direccion": direccion,
        "numero_telefono": numero_telefono,
        "correo_electronico": correo_electronico,
        "nombre_contacto_emergencia": nombre_contacto_emergencia,
        "relacion_con_paciente": relacion_con_paciente,
        "numero_telefono_emergencia": numero_telefono_emergencia,
        "nombre_compania_seguros": nombre_compania_seguros,
        "numero_poliza": numero_poliza,
        "estado_poliza": estado_poliza
    }

    return paciente

def agendar_cita(pacientes):
    print("----- Agendar Cita -----")
    
    cedula = input("Cédula del paciente: ")
    paciente = next((p for p in pacientes if p['cedula'] == cedula), None)

    if not paciente:
        print("Paciente no encontrado!")
        return

    fecha_cita = input("Fecha de la cita (DD/MM/YYYY): ")
    while not validar_fecha(fecha_cita):
        fecha_cita = input("Fecha de cita inválida. Ingrese una fecha en formato DD/MM/YYYY: ")

    hora_cita = input("Hora de la cita (HH:MM): ")

    nueva_cita = {
        "nombre_paciente": paciente["nombre"],
        "cedula_paciente": paciente["cedula"],
        "fecha_cita": fecha_cita,
        "hora_cita": hora_cita,
    }

    return nueva_cita
def obtener_info_paciente(cedula_paciente, lista_pacientes):
    # Retorna la información del paciente basada en su cédula
    return next((paciente for paciente in lista_pacientes if paciente["cedula"] == cedula_paciente), None)


def obtener_historia_clinica(cedula_paciente):
    # Esta función retorna la historia clínica basada en la cédula del paciente
    return me.historia_clinica_db.get(cedula_paciente, {})

def generar_factura(cedula_paciente):
    paciente = obtener_info_paciente(cedula_paciente)
    historia = obtener_historia_clinica(cedula_paciente)
    if not paciente or not historia:
        print("No se encontró información del paciente o su historia clínica.")
        return

    print("\n------- Facturación -------")
    print(f"Nombre del paciente: {paciente['nombre']}")
    print(f"Edad: {paciente['edad']}")
    print(f"Cédula: {cedula_paciente}")
    # Tomando la última consulta del paciente como referencia
    ultima_consulta = list(historia.values())[-1]
    print(f"Nombre del médico tratante: {ultima_consulta['cedula_medico']}")  # Aquí deberíamos traducir la cédula a nombre usando un DB adecuado
    print(f"Nombre de la compañía de seguro: {paciente['compania_seguro']}")
    print(f"Numero de póliza: {paciente['numero_poliza']}")
    print(f"Vigencia de la póliza: {'Activa' if paciente['poliza_activa'] else 'Inactiva'}")

    # Calcular y desglosar costos
    total = 0
    for orden in me.ordenes_db:
        if orden["cedula_paciente"] == cedula_paciente:
            if orden["tipo_orden"] == "medicamentos":
                for med in me.ordenes_medicamento_db:
                    if med["numero_orden"] == orden["numero_orden"]:
                        print(f"Medicamento: {med['nombre_medicamento']} - Costo: ${med['costo']} - Dosis: {med['dosis']}")
                        total += int(med["costo"])
            elif orden["tipo_orden"] == "procedimientos":
                for proc in me.ordenes_procedimiento_db:
                    if proc["numero_orden"] == orden["numero_orden"]:
                        print(f"Procedimiento: {proc['nombre_procedimiento']} - Costo: ${proc['costo']}")
                        total += int(proc["costo"])
            # Agregar condición para ayuda diagnóstica si se implementa

    if paciente['poliza_activa']:
        total_copagos = COPAGO * len(historia)
        if total_copagos <= LIMITE_COPAGO:
            print(f"\nTotal a pagar por el paciente (Copago): ${COPAGO}")
            print(f"Total a pagar por la aseguradora: ${total - COPAGO}")
        else:
            print(f"\nTotal a pagar por el paciente (Copago): $0 (Límite de copago alcanzado)")
            print(f"Total a pagar por la aseguradora: ${total}")
    else:
        print(f"\nTotal a pagar por el paciente: ${total}")

    print("-----------------------------")

# Para probar la función, puedes llamar:
# generar_factura('cedula_del_paciente')


def menu_administrativo():
    pacientes = []
    citas = []
    facturas = []

    while True:
        print("Sistema Administrativo")
        print("1. Registrar paciente")
        print("2. Agendar cita")
        print("3. Registrar factura")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            paciente = registrar_paciente()
            pacientes.append(paciente)
            print("¡Paciente registrado exitosamente!")
        elif opcion == "2":
            cita = agendar_cita(pacientes)
            if cita:
                citas.append(cita)
                print("¡Cita agendada exitosamente!")

        elif opcion == "3":
            cedula_paciente = input("Ingrese la cédula del paciente para generar la factura: ")
            factura = generar_factura(cedula_paciente)
            if factura:
                facturas.append(factura)
                print("\n¡Factura registrada exitosamente!")

        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
