import json
import os

ARCHIVO = "reclamos.json"

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def guardar_datos(lista_reclamos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(lista_reclamos, archivo, indent=4, ensure_ascii=False)
