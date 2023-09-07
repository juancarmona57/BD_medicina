from medico import menu_medico
from enfermeras import *
from personal_administrativo import *
from recursos_humanos import *

def menu_principal():
    personas = []
    medicos = []
    enfermeras = []
    administrativos = []

    while True:
        print("Sistema Hospitalario")
        print("1. Recursos Humanos")
        print("2. Enfermera")
        print("3. Médico")
        print("4. Personal Administrativo")
        print("5. Salir")
        opcion = input("Seleccione un rol: ")

        if opcion == "1":
            menu_recursos_humanos()
        elif opcion == "2":
            menu_enfermera()
        elif opcion == "3":
            menu_medico()  # Aquí pasamos la lista de personas a menu_medico
        elif opcion == "4":
            menu_administrativo()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    menu_principal()

