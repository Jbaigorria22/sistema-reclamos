import sqlite3

DB_NAME = "reclamos.db"


def get_connection():
    """
    Devuelve una conexión a la base de datos
    """
    return sqlite3.connect(DB_NAME)


def crear_tabla():
    """
    Crea la tabla reclamos si no existe
    """
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reclamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            barrio TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            fecha TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()
def crear_tabla_usuarios():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    conexion.commit()
    conexion.close()

