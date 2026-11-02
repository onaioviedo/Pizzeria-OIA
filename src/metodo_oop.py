"""Método 2: versión con clases y objetos (POO)."""
from src.clases.pizzeria import Pizzeria


def ejecutar_metodo_2():
    print("\n=== EJECUTANDO MÉTODO 2 (POO) ===")
    Pizzeria().tomar_pedido()


if __name__ == "__main__":
    ejecutar_metodo_2()