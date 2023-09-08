# Suponiendo que esta parte del código está en un archivo llamado "medico.py"

# Importamos la lista de personas del archivo de recursos humanos y pacientes de personal administrativo
from recursos_humanos import personas
from personal_administrativo import pacientes

historia_clinica_db = {}  # Este diccionario simulará nuestra base de datos NoSQL.

def medico_existe(cedula):
    for persona in personas:
        if persona['cedula'] == cedula and persona['rol'] == 'medico':
            return True
    return False

def paciente_existe(cedula):
    return cedula in [paciente['cedula'] for paciente in pacientes]

def registrar_historia_clinica():
    print("----- Registro de Historia Clínica -----")

    cedula_paciente = input("Cédula del paciente: ")

    # Verificar si el paciente existe
    while not paciente_existe(cedula_paciente):
        print("La cédula ingresada no corresponde a un paciente registrado.")
        cedula_paciente = input("Cédula del paciente: ")

    # Si la cédula del paciente no existe en la base de historia clínica, se crea una nueva entrada para él.
    if cedula_paciente not in historia_clinica_db:
        historia_clinica_db[cedula_paciente] = {}

    fecha_atencion = input("Fecha de atención (DD/MM/YYYY): ")

    cedula_medico = input("Cédula del médico que lo atendió (10 dígitos máx.): ")
    while len(cedula_medico) > 10 or not medico_existe(cedula_medico):
        print("Verifique que la cédula tenga 10 dígitos y corresponda a un médico registrado.")
        cedula_medico = input("Cédula del médico que lo atendió (10 dígitos máx.): ")

    motivo_consulta = input("Motivo de la consulta: ")
    sintomatologia = input("Sintomatología: ")
    diagnostico = input("Diagnóstico: ")

    # Se crea el registro de la consulta
    registro_consulta = {
        "cedula_medico": cedula_medico,
        "motivo_consulta": motivo_consulta,
        "sintomatologia": sintomatologia,
        "diagnostico": diagnostico
    }

    # Se añade el registro a la historia clínica del paciente bajo la fecha de atención.
    historia_clinica_db[cedula_paciente][fecha_atencion] = registro_consulta
    print("Historial clínico actualizado con éxito!")

# El resto del código sigue igual


