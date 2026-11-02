from data import data
from src.functions import obtener_temporada
from src.clases.carta import Carta
from src.clases.carrito import Carrito, Comensal
from src.clases.ofertas import GestorOfertas

RESPUESTAS_SI = ("s", "si", "sí")


class Pizzeria:
    """Pizzería: calcula costes según la temporada y gestiona el pedido por consola."""

    def __init__(self, fecha=None):
        self.temporada = obtener_temporada(fecha)
        self.pizzas_estimadas_mes = data.TEMPORADAS_VENTAS[self.temporada]
        self.coste_fijo_por_pizza = (data.gasto_personal_mensual + data.gasto_alquiler_mensual) / self.pizzas_estimadas_mes
        self.carta = Carta(self.coste_fijo_por_pizza)
        self.ofertas = GestorOfertas()
        self.carrito = Carrito()

    def pedir_oferta(self):
        self.ofertas.mostrar()
        opciones = self.ofertas.opciones_validas()
        while True:
            opcion = input(f"Elige una opción (1-{opciones[-1]}): ").strip()
            if opcion in opciones:
                return self.ofertas.por_opcion(opcion)
            print(f"Opción no válida. Elige un número del 1 al {opciones[-1]}.")

    def pedir_pizza(self):
        print("\nPizzas disponibles:")
        self.carta.mostrar_pizzas()
        while True:
            pizza = self.carta.buscar_pizza(input("Elige una pizza: "))
            if pizza is not None:
                return pizza
            print("No se ha encontrado esa pizza, vuelve a introducirla.")

    def pedir_bebida(self):
        self.carta.mostrar_bebidas()
        while True:
            bebida = self.carta.buscar_bebida(input("Elige una bebida: "))
            if bebida is not None:
                return bebida
            print("No se ha encontrado esa bebida, vuelve a introducirla.")

    def atender_comensal(self, numero):
        print(f"\n--- COMENSAL {numero} ---")
        comensal = Comensal(numero, self.pedir_oferta())

        comensal.pizza = self.pedir_pizza()
        if comensal.tiene_oferta("2x1") and comensal.pizza.nombre not in data.PIZZAS_2X1:
            print(f"La pizza {comensal.pizza.nombre} no está incluida en la oferta 2x1.")

        respuesta_bebida = input("¿Quieres añadir una bebida? (s/n): ").strip().lower()
        if respuesta_bebida in RESPUESTAS_SI:
            comensal.bebida = self.pedir_bebida()
        elif comensal.tiene_oferta("menu"):
            print("La oferta de menú necesita una pizza y una bebida; no se aplicará a este comensal.")

        self.carrito.agregar_comensal(comensal)

    def falta_minimo_volumen(self):
        """True si se eligió el descuento por volumen y el pedido aún no llega al mínimo."""
        volumen = self.ofertas.buscar("volumen")
        return volumen in self.carrito.ofertas_elegidas() and not volumen.alcanza_minimo(self.carrito)

    def tomar_pedido(self):
        numero_comensal = 1
        continuar = True
        while continuar:
            self.atender_comensal(numero_comensal)

            if self.falta_minimo_volumen():
                print(f"Para finalizar con la oferta del 10%, el pedido debe llegar a "
                      f"{data.LIMITE_DESCUENTO_VOLUMEN:.2f} €. Añade otro comensal.")
                numero_comensal += 1
                continue

            respuesta_comensal = input("¿Quieres añadir otro comensal? (s/n): ").strip().lower()
            if respuesta_comensal not in RESPUESTAS_SI:
                continuar = False
            numero_comensal += 1

        self.mostrar_resumen()

    def mostrar_resumen(self):
        descuentos = self.ofertas.aplicar(self.carrito)

        oferta_2x1 = self.ofertas.buscar("2x1")
        if oferta_2x1 in self.carrito.ofertas_elegidas() and not any(texto == oferta_2x1.nombre for texto, importe in descuentos):
            promocionadas = ", ".join(data.PIZZAS_2X1[:-1]) + " o " + data.PIZZAS_2X1[-1]
            print(f"El 2x1 requiere dos pizzas promocionadas: {promocionadas}.")

        print("\n--- RESUMEN FINAL ---")
        print(self.carrito.ticket(data.iva, descuentos))


def ejecutar():
    """Punto de entrada del modo con clases y objetos."""
    Pizzeria().tomar_pedido()


if __name__ == "__main__":
    ejecutar()
