import csv
from gestion_reclamos import reclamos


def exportar_pendientes_csv():
    pendientes = [r for r in reclamos if r["estado"] == "Pendiente"]

    if not pendientes:
        print("No hay reclamos pendientes para exportar.")
        return

    with open("pendientes.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=pendientes[0].keys())
        writer.writeheader()
        writer.writerows(pendientes)

    print("Reclamos pendientes exportados a pendientes.csv")


def exportar_por_barrio():
    barrio = input("Ingrese barrio a exportar: ").lower()
    filtrados = [r for r in reclamos if r["barrio"].lower() == barrio]

    if not filtrados:
        print("No hay reclamos para ese barrio.")
        return

    nombre_archivo = f"reclamos_{barrio}.csv"

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=filtrados[0].keys())
        writer.writeheader()
        writer.writerows(filtrados)

    print(f"Reclamos exportados a {nombre_archivo}")
