from database import get_connection
from datetime import datetime


def crear_reclamo(nombre, barrio, descripcion):
    conn = get_connection()
    cursor = conn.cursor()

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    estado = "Pendiente"

    cursor.execute("""
        INSERT INTO reclamos (nombre, barrio, descripcion, fecha, estado)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, barrio, descripcion, fecha, estado))

    conn.commit()
    conn.close()


def obtener_reclamos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reclamos ORDER BY id DESC")
    reclamos = cursor.fetchall()

    conn.close()
    return reclamos


def cambiar_estado_reclamo(id_reclamo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE reclamos
        SET estado = 'Resuelto'
        WHERE id = ?
    """, (id_reclamo,))

    conn.commit()
    conn.close()

def cambiar_estado_reclamo(id_reclamo, nuevo_estado):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE reclamos SET estado = ? WHERE id = ?",
        (nuevo_estado, id_reclamo)
    )

    conn.commit()
    conn.close()
