class Comensal:
    """Comensal del pedido: una pizza, una bebida opcional y la oferta elegida."""

    def __init__(self, numero, oferta=None):
        self.numero = numero
        self.oferta = oferta      # objeto Oferta o None
        self.pizza = None
        self.bebida = None

    def productos(self):
        """Lista de productos del comensal (pizza y, si la hay, bebida)."""
        productos = []
        if self.pizza is not None:
            productos.append(self.pizza)
        if self.bebida is not None:
            productos.append(self.bebida)
        return productos

    def tiene_oferta(self, clave):
        return self.oferta is not None and self.oferta.clave == clave


class Carrito:
    """Carrito con los comensales del pedido."""

    def __init__(self):
        self.comensales = []

    def agregar_comensal(self, comensal):
        self.comensales.append(comensal)

    def productos(self):
        productos = []
        for comensal in self.comensales:
            productos.extend(comensal.productos())
        return productos

    def subtotal(self):
        return sum(producto.precio for producto in self.productos())

    def ofertas_elegidas(self):
        """Ofertas distintas elegidas por los comensales, en orden de elección."""
        ofertas = []
        for comensal in self.comensales:
            if comensal.oferta is not None and comensal.oferta not in ofertas:
                ofertas.append(comensal.oferta)
        return ofertas
