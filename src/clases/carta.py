from data import data
from src.clases.productos import Pizza, Bebida


class Carta:
    """Carta de la pizzería: pizzas y bebidas creadas a partir de data.py."""

    def __init__(self, coste_fijo_por_pizza):
        self.pizzas = []
        for nombre, ingredientes in data.pizzas.items():
            pizza = Pizza(nombre, ingredientes)
            pizza.precio = pizza.calcular_precio(coste_fijo_por_pizza)
            self.pizzas.append(pizza)

        self.bebidas = []
        for nombre, precio in data.BEBIDAS.items():
            self.bebidas.append(Bebida(nombre.title(), precio))

    def buscar_pizza(self, nombre):
        """Devuelve la pizza con ese nombre (sin distinguir mayúsculas) o None."""
        for pizza in self.pizzas:
            if pizza.nombre.lower() == nombre.strip().lower():
                return pizza
        return None

    def buscar_bebida(self, nombre):
        """Devuelve la bebida con ese nombre (sin distinguir mayúsculas) o None."""
        for bebida in self.bebidas:
            if bebida.nombre.lower() == nombre.strip().lower():
                return bebida
        return None

    def mostrar_pizzas(self):
        for pizza in self.pizzas:
            print(pizza.descripcion())

    def mostrar_bebidas(self):
        print("Bebidas disponibles: " + ", ".join(bebida.nombre.lower() for bebida in self.bebidas))
