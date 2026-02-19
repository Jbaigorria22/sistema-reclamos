import os
from datetime import datetime

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def obtener_fecha_actual():
    return datetime.now().strftime("%d/%m/%Y %H:%M")
