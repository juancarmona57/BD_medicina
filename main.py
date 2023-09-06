from recursos_humanos import Persona as RecursosHumanos
from enfermeras import Enfermera
from medico import Medico
from personal_administrativo import RegistroPacientes, Factura

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
            rh = RecursosHumanos()
            rh.main()
        elif opcion == "2":
            enfermera_handler = Enfermera()
            enfermera_handler.menu_principal()
        elif opcion == "3":
            medico_handler = Medico()
            medico_handler.menu_principal()
        elif opcion == "4":
            personal_admin_handler = RegistroPacientes()
            factura_handler = Factura(personal_admin_handler.base_datos)
            personal_admin_handler.main()  # Aquí podría haber un menú específico para el Personal Administrativo si se desea.
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    menu_principal()
