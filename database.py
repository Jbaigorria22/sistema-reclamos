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
            dni TEXT NOT NULL,
            nro_socio TEXT NOT NULL,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            estado TEXT DEFAULT 'Pendiente'
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
    # Usuario por defecto para administración
    cursor.execute("INSERT OR IGNORE INTO usuarios (username, password) VALUES ('admin', '1234')")
    conn.commit()
    conn.close()