# controladores.py

# Simulación de una base de datos de pacientes
pacientes_db = []

# Simulación de una base de datos de historias clínicas
historia_clinica_db = {}

def registrar_paciente_controlador(datos_paciente):
    """
    Registra un nuevo paciente en la base de datos.
    
    Argumentos:
    - datos_paciente: Diccionario con los datos del paciente
    
    Retorna:
    - 'exito': Verdadero si el registro fue exitoso, Falso de lo contrario
    - 'mensaje': Mensaje detallado sobre el resultado de la operación
    """
    # Validación de datos
    if 'cedula' not in datos_paciente:
        return {'exito': False, 'mensaje': 'La cédula es obligatoria para el registro.'}
    
    # Comprobación de idempotencia
    for paciente in pacientes_db:
        if paciente['cedula'] == datos_paciente['cedula']:
            return {'exito': False, 'mensaje': 'Un paciente con esta cédula ya está registrado.'}
            
    # Registro del paciente
    pacientes_db.append(datos_paciente)
    return {'exito': True, 'mensaje': 'Paciente registrado con éxito.'}

def registrar_historia_clinica_controlador(cedula_paciente, datos_clinicos):
    """
    Registra una nueva entrada en la historia clínica de un paciente.
    
    Argumentos:
    - cedula_paciente: Cédula del paciente
    - datos_clinicos: Diccionario con los datos clínicos
    
    Retorna:
    - 'exito': Verdadero si el registro fue exitoso, Falso de lo contrario
    - 'mensaje': Mensaje detallado sobre el resultado de la operación
    """
    # Validación de datos
    if not cedula_paciente or not datos_clinicos:
        return {'exito': False, 'mensaje': 'La cédula del paciente y los datos clínicos son obligatorios.'}
    
    # Comprobación de existencia del paciente
    existe_paciente = False
    for paciente in pacientes_db:
        if paciente['cedula'] == cedula_paciente:
            existe_paciente = True
            break
            
    if not existe_paciente:
        return {'exito': False, 'mensaje': 'El paciente con esta cédula no está registrado.'}
    
    # Registro de la historia clínica
    if cedula_paciente not in historia_clinica_db:
        historia_clinica_db[cedula_paciente] = []
        
    historia_clinica_db[cedula_paciente].append(datos_clinicos)
    return {'exito': True, 'mensaje': 'Historia clínica registrada con éxito.'}
