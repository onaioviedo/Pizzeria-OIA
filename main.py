
import argparse
import sys

from src.metodo_procedural import ejecutar_metodo_1
from src.metodo_oop import ejecutar_metodo_2


def mostrar_menu():
    while True:
        print("\n--- ELIGE EL MÉTODO DE EJECUCIÓN ---")
        print("1. Método 1 (Programación básica: bucles y funciones)")
        print("2. Método 2 (POO: Clases, objetos, herencia y super)")
        print("3. Salir")

        eleccion = input("Elige una opción (1-3): ").strip()

        if eleccion == "1":
            ejecutar_metodo_1()
        elif eleccion == "2":
            ejecutar_metodo_2()
        elif eleccion == "3":
            print("¡Hasta luego!")
            sys.exit()
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def main():
    parser = argparse.ArgumentParser(description="Pizzería OIA: caja registradora por consola.")
    parser.add_argument(
        "metodo",
        nargs="?",
        choices=["procedural", "1", "oop", "2"],
        help="método a ejecutar; si se omite, se muestra el menú",
    )
    argumentos = parser.parse_args()

    if argumentos.metodo in ("procedural", "1"):
        ejecutar_metodo_1()
    elif argumentos.metodo in ("oop", "2"):
        ejecutar_metodo_2()
    else:
        mostrar_menu()


if __name__ == "__main__":
    main()