import pyodbc

class Medico:
    def __init__(self):
        # Conexión a la base de datos
        self.conn = self.conectar_sql_server()
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def conectar_sql_server(self):
        # Datos de conexión a tu base de datos
        server = 'NOMBRE_DEL_SERVIDOR'
        database = 'NOMBRE_DE_LA_BASE_DE_DATOS'
        username = 'USUARIO'
        password = 'CONTRASEÑA'
        driver = '{ODBC Driver 17 for SQL Server}'

        # Establece la conexión
        return pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

    def crear_tablas(self):
        # Creación de tablas si no existen
        self.cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ordenes' AND xtype='U')
        CREATE TABLE ordenes (
            numero_orden INT PRIMARY KEY,
            cedula_paciente VARCHAR(10),
            cedula_medico VARCHAR(10),
            fecha_creacion DATE,
            tipo_orden VARCHAR(50)
        )
        """)

        self.cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ordenes_medicamentos' AND xtype='U')
        CREATE TABLE ordenes_medicamentos (
            numero_orden INT,
            numero_item INT,
            medicamento VARCHAR(100),
            dosis VARCHAR(50),
            duracion VARCHAR(50),
            costo FLOAT,
            PRIMARY KEY (numero_orden, numero_item)
        )
        """)

        self.cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ordenes_procedimientos' AND xtype='U')
        CREATE TABLE ordenes_procedimientos (
            numero_orden INT,
            numero_item INT,
            procedimiento VARCHAR(100),
            veces_repite INT,
            frecuencia_repite VARCHAR(50),
            costo FLOAT,
            requiere_especialista BIT,
            PRIMARY KEY (numero_orden, numero_item)
        )
        """)

        self.conn.commit()

    def registrar_orden_medicamento(self, cedula_paciente, cedula_medico, fecha, medicamentos):
        self.cursor.execute("INSERT INTO ordenes (cedula_paciente, cedula_medico, fecha_creacion, tipo_orden) VALUES (?, ?, ?, 'medicamento')", (cedula_paciente, cedula_medico, fecha))
        numero_orden = self.cursor.lastrowid
        for medicamento in medicamentos:
            self.cursor.execute("INSERT INTO ordenes_medicamentos (numero_orden, medicamento, dosis, duracion, costo) VALUES (?, ?, ?, ?, ?)", (numero_orden, medicamento['nombre'], medicamento['dosis'], medicamento['duracion'], medicamento['costo']))
        self.conn.commit()

    def registrar_orden_procedimiento(self, cedula_paciente, cedula_medico, fecha, procedimientos):
        self.cursor.execute("INSERT INTO ordenes (cedula_paciente, cedula_medico, fecha_creacion, tipo_orden) VALUES (?, ?, ?, 'procedimiento')", (cedula_paciente, cedula_medico, fecha))
        numero_orden = self.cursor.lastrowid
        for procedimiento in procedimientos:
            self.cursor.execute("INSERT INTO ordenes_procedimientos (numero_orden, procedimiento, veces_repite, frecuencia_repite, costo, requiere_especialista) VALUES (?, ?, ?, ?, ?, ?)", (numero_orden, procedimiento['nombre'], procedimiento['veces'], procedimiento['frecuencia'], procedimiento['costo'], procedimiento['especialista']))
        self.conn.commit()

    def menu_principal(self):
        while True:
            print("Sistema Médico")
            print("1. Registrar historia clínica")
            print("2. Prescribir medicamentos")
            print("3. Solicitar procedimientos")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Aquí iría el código para registrar historia clínica
                pass
            elif opcion == "2":
                # Aquí iría el código para prescribir medicamentos
                pass
            elif opcion == "3":
                # Aquí iría el código para solicitar procedimientos
                pass
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, elija una opción válida.")

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    medico_handler = Medico()
    medico_handler.menu_principal()
