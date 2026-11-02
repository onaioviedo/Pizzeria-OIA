# Archivo principal
import sys
from metodo_procedural import ejecutar_metodo_1
from metodo_oop import ejecutar_metodo_2

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