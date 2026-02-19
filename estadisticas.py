from datos import cargar_datos

def mostrar_estadisticas():
    reclamos = cargar_datos()

    if not reclamos:
        print("\nNo hay reclamos cargados.")
        return

    total = len(reclamos)

    pendientes = sum(1 for r in reclamos if r["estado"] == "Pendiente")
    resueltos = sum(1 for r in reclamos if r["estado"] == "Resuelto")

    print("\n--- ESTADÍSTICAS ---")
    print(f"Total de reclamos: {total}")
    print(f"Pendientes: {pendientes}")
    print(f"Resueltos: {resueltos}")
