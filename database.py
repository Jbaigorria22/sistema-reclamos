import sqlite3

def get_connection():
    conn = sqlite3.connect("reclamos.db")
    conn.row_factory = sqlite3.Row
    return conn

def crear_tabla():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reclamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dni TEXT,
            nombre TEXT,
            direccion TEXT,
            tipo TEXT,
            descripcion TEXT,
            estado TEXT
        )
    """)
    conn.commit()
    conn.close()

def crear_tabla_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    # Borramos el admin viejo y creamos el nuevo con 1234 para estar seguros
    cursor.execute("DELETE FROM usuarios WHERE username='admin'")
    cursor.execute("INSERT INTO usuarios (username, password) VALUES ('admin', '1234')")
    conn.commit()
    conn.close()