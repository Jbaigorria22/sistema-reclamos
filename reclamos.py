from gestion_reclamos import (
    cargar_reclamo,
    listar_reclamos,
    ver_pendientes,
    marcar_como_resuelto,
    buscar_por_barrio,
    buscar_por_numero,
    mostrar_estadisticas,
    exportar_pendientes_csv
)

from utils import limpiar_pantalla


def mostrar_menu():
    print("SISTEMA DE RECLAMOS")
    print("1 - Cargar reclamo")
    print("2 - Listar reclamos")
    print("3 - Ver pendientes")
    print("4 - Marcar reclamo como resuelto")
    print("5 - Buscar por número")
    print("6 - Buscar por barrio")
    print("7 - Ver estadísticas")
    print("8 - Exportar pendientes a CSV")
    print("9 - Salir")


def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            cargar_reclamo()

        elif opcion == "2":
            listar_reclamos()

        elif opcion == "3":
            ver_pendientes()

        elif opcion == "4":
            marcar_como_resuelto()

        elif opcion == "5":
            buscar_por_numero()

        elif opcion == "6":
            buscar_por_barrio()

        elif opcion == "7":
            mostrar_estadisticas()

        elif opcion == "8":
            exportar_pendientes_csv()

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")
            input("Presione ENTER para continuar...")


if __name__ == "__main__":
    main()
