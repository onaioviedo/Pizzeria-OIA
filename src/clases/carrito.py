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

    def ticket(self, iva, descuentos=None):
        """Ticket: productos, descuentos de ofertas, base, IVA y total."""
        if descuentos is None:
            descuentos = []
        output = "Productos:\n"
        for producto in self.productos():
            output += f"- {producto}\n"

        total_descuentos = 0
        if len(descuentos) > 0:
            output += "\nDescuentos:\n"
            for texto, importe in descuentos:
                total_descuentos += importe
                output += f"- {texto}: -{importe:.2f} €\n"

        base = self.subtotal() - total_descuentos
        importe_iva = base * iva
        output += f"\nDescuento total: {total_descuentos:.2f} €\n"
        output += f"\nBase imponible: {base:.2f} €\n"
        output += f"IVA: {importe_iva:.2f} €\n"
        output += f"Total: {base + importe_iva:.2f} €\n"
        return output
