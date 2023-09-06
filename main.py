from recursos_humanos import main as rh_main
from enfermeras import main as enfermera_main
from medico import Medico
from personal_administrativo import main as pa_main

def menu_principal():
    while True:
        print("\nSistema Hospitalario")
        print("1. Recursos Humanos")
        print("2. Enfermera")
        print("3. Médico")
        print("4. Personal Administrativo")
        print("5. Salir")

        opcion = input("Seleccione un rol: ")

        if opcion == "1":
            rh_main()
        elif opcion == "2":
            enfermera_main()
        elif opcion == "3":
            medico_handler = Medico()
            medico_handler.menu_principal()
        elif opcion == "4":
            pa_main() # Aquí podría haber un menú específico para el Personal Administrativo si se desea.
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    menu_principal()
