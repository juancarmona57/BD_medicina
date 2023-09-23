import re
from datetime import datetime

class RecursosHumanos:
    personas = []

    @classmethod
    def validar_correo(cls, correo):
        return re.match(r'^[\w\.-]+@[\w\.-]+$', correo)

    @classmethod
    def validar_telefono(telefono):
        return re.match(r'^\d{10}$', telefono)

    @classmethod
    def validar_cedula(cedula):
        global personas
        return re.match(r'^\d{10}$', cedula) and cedula not in [persona['cedula'] for persona in personas]

    @classmethod
    def validar_fecha(fecha):
        try:
            datetime.strptime(fecha, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    @classmethod
    def validar_contraseña(contraseña):
        return (any(c.isupper() for c in contraseña) and
                any(c.isdigit() for c in contraseña) and
                any(c in '!@#$%^&*()_-+={}[]|\:;"<>,.?/~' for c in contraseña) and
                len(contraseña) >= 8)

    @classmethod
    def registrar_persona(cls):
        global personas

        nombre = input("Nombre completo: ")
        while True:
            cedula = input("Número de cédula: ")
            if not cls.validar_cedula(cedula):
                print("Verificar cédula número de caracteres o cédula ya registrada.")
            else:
                break

        correo = input("Correo electrónico: ")
        while not cls.validar_correo(correo):
            correo = input("Correo electrónico inválido. Ingrese un correo válido: ")

        telefono = input("Número de teléfono: ")
        while not cls.validar_telefono(telefono):
            telefono = input("Número de teléfono inválido. Ingrese un número de 10 dígitos: ")

        fecha_nacimiento = input("Fecha de nacimiento (DD/MM/YYYY): ")
        while not cls.validar_fecha(fecha_nacimiento):
            fecha_nacimiento = input("Fecha de nacimiento inválida. Ingrese una fecha en formato DD/MM/YYYY: ")

        direccion = input("Dirección (máximo 30 caracteres): ")[:30]
        rol = input("Rol: ")
        usuario = input("Nombre de usuario: ")
        contraseña = input("Contraseña: ")

        while not cls.validar_contraseña(contraseña):
            contraseña = input("Contraseña inválida. Debe incluir al menos una mayúscula, un número, un carácter especial y tener al menos 8 caracteres: ")

        nueva_persona = {
            "nombre": nombre, 
            "cedula": cedula, 
            "correo": correo, 
            "telefono": telefono,
            "fecha_nacimiento": fecha_nacimiento, 
            "direccion": direccion, 
            "rol": rol,
            "usuario": usuario, 
            "contraseña": contraseña
        }

        cls.personas.append(nueva_persona)
        print("¡Persona registrada exitosamente!")

    @classmethod
    def eliminar_persona(cls):
        global personas

        cedula_eliminar = input("Ingrese la cédula de la persona que desea eliminar: ")
        cls.personas = [persona for persona in personas if persona['cedula'] != cedula_eliminar]
        print("¡Persona eliminada exitosamente!")

    @classmethod
    def mostrar_personas(cls):
        global personas

        for persona in cls.personas:
            print(f"Nombre: {persona['nombre']}")
            print(f"Cédula: {persona['cedula']}")
            print(f"Correo: {persona['correo']}")
            print(f"Teléfono: {persona['telefono']}")
            print(f"Fecha de Nacimiento: {persona['fecha_nacimiento']}")
            print(f"Dirección: {persona['direccion']}")
            print(f"Rol: {persona['rol']}")
            print(f"Usuario: {persona['usuario']}")
            print("----------------------")

    @classmethod
    def menu_recursos_humanos(cls):
        global personas

        while True:
            print("Registro de Personas")
            print("1. Registrar nueva persona")
            print("2. Mostrar todas las personas registradas")
            print("3. Eliminar persona")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cls.registrar_persona()
            elif opcion == "2":
                cls.mostrar_personas()
            elif opcion == "3":
                cls.eliminar_persona()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, elija una opción válida.")
