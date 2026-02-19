import json
import os
import csv
from datetime import datetime
from modelo import Reclamo

ARCHIVO = "reclamos.json"


# =========================
# UTILIDADES
# =========================

def obtener_fecha_actual():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []


def guardar_datos(reclamos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(reclamos, archivo, indent=4, ensure_ascii=False)


# =========================
# CARGAR RECLAMO
# =========================

def cargar_reclamo():
    reclamos = cargar_datos()

    print("\n--- CARGAR RECLAMO ---")

    while True:
        nombre = input("Nombre del vecino: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    while True:
        barrio = input("Barrio: ").strip()
        if barrio:
            break
        print("El barrio no puede estar vacío.")

    while True:
        descripcion = input("Descripción del reclamo: ").strip()
        if descripcion:
            break
        print("La descripción no puede estar vacía.")

    if reclamos:
        nuevo_numero = reclamos[-1]["numero_servicio"] + 1
    else:
        nuevo_numero = 1

    nuevo_reclamo = Reclamo(
        nuevo_numero,
        nombre,
        barrio,
        descripcion,
        obtener_fecha_actual()
    )

    reclamos.append(nuevo_reclamo.to_dict())
    guardar_datos(reclamos)

    print("\nReclamo cargado correctamente.")
    input("Presione ENTER para continuar...")


# =========================
# LISTAR RECLAMOS
# =========================

def listar_reclamos():
    reclamos = cargar_datos()

    if not reclamos:
        print("No hay reclamos cargados.")
        input("Presione ENTER para continuar...")
        return

    print("\n--- LISTA DE RECLAMOS ---")
    for r in reclamos:
        print(f"""
Número: {r['numero_servicio']}
Nombre: {r['nombre']}
Barrio: {r['barrio']}
Descripción: {r['descripcion']}
Fecha: {r['fecha']}
Estado: {r['estado']}
---------------------------
""")

    input("Presione ENTER para continuar...")


# =========================
# VER PENDIENTES
# =========================

def ver_pendientes():
    reclamos = cargar_datos()
    pendientes = [r for r in reclamos if r["estado"] == "Pendiente"]

    if not pendientes:
        print("No hay reclamos pendientes.")
        input("Presione ENTER para continuar...")
        return

    print("\n--- RECLAMOS PENDIENTES ---")
    for r in pendientes:
        print(f"""
Número: {r['numero_servicio']}
Nombre: {r['nombre']}
Barrio: {r['barrio']}
Descripción: {r['descripcion']}
Fecha: {r['fecha']}
Estado: {r['estado']}
---------------------------
""")

    input("Presione ENTER para continuar...")


# =========================
# MARCAR COMO RESUELTO
# =========================

def marcar_como_resuelto():
    reclamos = cargar_datos()

    if not reclamos:
        print("No hay reclamos cargados.")
        input("Presione ENTER para continuar...")
        return

    while True:
        numero = input("Ingrese número de servicio: ").strip()
        if numero.isdigit():
            break
        print("Debe ingresar un número válido.")

    numero = int(numero)
    encontrado = False

    for i, r in enumerate(reclamos):
        if r["numero_servicio"] == numero:
            reclamo_obj = Reclamo.from_dict(r)

            if reclamo_obj.marcar_como_resuelto():
                reclamos[i] = reclamo_obj.to_dict()
                guardar_datos(reclamos)
                print("Reclamo marcado como RESUELTO.")
            else:
                print("El reclamo ya estaba resuelto.")

            encontrado = True
            break

    if not encontrado:
        print("Reclamo no encontrado.")

    input("\nPresione ENTER para continuar...")


# =========================
# BUSCAR POR NÚMERO
# =========================

def buscar_por_numero():
    reclamos = cargar_datos()

    numero = input("Ingrese número de servicio: ").strip()

    if not numero.isdigit():
        print("Debe ingresar un número válido.")
        input("Presione ENTER para continuar...")
        return

    numero = int(numero)

    for r in reclamos:
        if r["numero_servicio"] == numero:
            print(f"""
Número: {r['numero_servicio']}
Nombre: {r['nombre']}
Barrio: {r['barrio']}
Descripción: {r['descripcion']}
Fecha: {r['fecha']}
Estado: {r['estado']}
""")
            input("Presione ENTER para continuar...")
            return

    print("Reclamo no encontrado.")
    input("Presione ENTER para continuar...")


# =========================
# BUSCAR POR BARRIO
# =========================

def buscar_por_barrio():
    reclamos = cargar_datos()
    barrio = input("Ingrese barrio a buscar: ").strip()

    encontrados = [r for r in reclamos if r["barrio"].lower() == barrio.lower()]

    if not encontrados:
        print("No se encontraron reclamos en ese barrio.")
        input("Presione ENTER para continuar...")
        return

    for r in encontrados:
        print(f"""
Número: {r['numero_servicio']}
Nombre: {r['nombre']}
Descripción: {r['descripcion']}
Fecha: {r['fecha']}
Estado: {r['estado']}
---------------------------
""")

    input("Presione ENTER para continuar...")


# =========================
# ESTADÍSTICAS
# =========================

def mostrar_estadisticas():
    reclamos = cargar_datos()

    total = len(reclamos)
    pendientes = len([r for r in reclamos if r["estado"] == "Pendiente"])
    resueltos = len([r for r in reclamos if r["estado"] == "Resuelto"])

    barrios = {}
    for r in reclamos:
        barrio = r["barrio"]
        barrios[barrio] = barrios.get(barrio, 0) + 1

    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    print(f"Total de reclamos: {total}")
    print(f"Pendientes: {pendientes}")
    print(f"Resueltos: {resueltos}")

    print("\nReclamos por barrio:")
    for barrio, cantidad in barrios.items():
        print(f"{barrio}: {cantidad}")

    input("\nPresione ENTER para continuar...")


# =========================
# EXPORTAR PENDIENTES
# =========================

def exportar_pendientes_csv():
    reclamos = cargar_datos()
    pendientes = [r for r in reclamos if r["estado"] == "Pendiente"]

    if not pendientes:
        print("No hay reclamos pendientes para exportar.")
        input("Presione ENTER para continuar...")
        return

    with open("reclamos_pendientes.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Numero", "Nombre", "Barrio", "Descripcion", "Fecha", "Estado"])

        for r in pendientes:
            writer.writerow([
                r["numero_servicio"],
                r["nombre"],
                r["barrio"],
                r["descripcion"],
                r["fecha"],
                r["estado"]
            ])

    print("Archivo 'reclamos_pendientes.csv' generado correctamente.")
    input("Presione ENTER para continuar...")
