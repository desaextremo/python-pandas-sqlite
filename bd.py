import sqlite3

def create_connection(db_file):
    """Crear una conexión a la base de datos SQLite especificada por db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexión a {db_file} establecida.")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Crear una tabla en la base de datos."""
    try:
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS estudiantes')
        conn.commit()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            genero TEXT NOT NULL,
            telefono TEXT,
            edad INTEGER	
        )
        ''')
        conn.commit()
        print("Tabla creada exitosamente")
    except sqlite3.Error as e:
        print(e)

def insert_estudiante(conn, estudiante):
    """Insertar un nuevo usuario en la tabla estudiantes."""
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO estudiantes (nombres, apellidos, email, genero, telefono)
        VALUES (?,?,?,?,?)''',estudiante)
        
        conn.commit()
        print("Estudiante insertado exitosamente")
    except sqlite3.Error as e:
        print(e)

def select_all_estudiantes(conn):
    """Consultar todos los registros de la tabla estudiantes."""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM estudiantes')
        rows = cursor.fetchall()
        for row in rows:
            #print(row)
            print(f"Id: {row[0]} Nombres: {row[1]} Apellidos: {row[2]} Email: {row[3]} Genero: {row[4]} Telefono: {row[5]} Edad: {row[6]}")
    except sqlite3.Error as e:
        print(e)

def select_estudiante(conn,idEstudiante):
    """Consultar datos del estudiante con id: idEstudiante."""
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM estudiantes
                          WHERE id = ?
                        ''',(idEstudiante,))
        rows = cursor.fetchall()
        print(f"Información del estudiante con id {idEstudiante}")
        for row in rows:
            #print(row)
            print(f"Id: {row[0]}\nNombres: {row[1]}\nApellidos: {row[2]}\nEmail: {row[3]}\nGenero: {row[4]}\nTelefono: {row[5]}\nEdad: {row[6]}")
    except sqlite3.Error as e:
        print(e)

def update_estudiante(conn, estudiante):
    """Actualizar la edad de un estudiante basado en su id."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE estudiantes 
        SET edad = ? 
        WHERE id = ?
        ''', estudiante)
        conn.commit()
        print(f"Usuario actualizado exitosamente :{estudiante[1]}")
    except sqlite3.Error as e:
        print(e)

def delete_estudiante(conn, idEstudiante):
    """Eliminar un estudiante basado en su id."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM estudiantes 
        WHERE id = ?
        ''', (idEstudiante,))
        conn.commit()
        print("estudiante eliminado exitosamente")
    except sqlite3.Error as e:
        print(e)