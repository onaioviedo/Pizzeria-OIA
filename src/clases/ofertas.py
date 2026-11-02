from data import data


class Oferta:
    """Oferta base: cada subclase calcula su propio descuento."""

    clave = None
    nombre = "Oferta"

    def descripcion(self):
        return self.nombre

    def calcular_descuento(self, carrito, descuentos_previos=0):
        """Importe a descontar (sin IVA). Las subclases lo sobrescriben."""
        return 0.0


class Oferta2x1(Oferta):
    """Por cada 2 pizzas de la lista 2x1, la más barata es gratis."""

    clave = "2x1"
    nombre = "Oferta 2x1"

    def descripcion(self):
        return f"2x1 por cada 2 pizzas de: {', '.join(data.PIZZAS_2X1)}"

    def calcular_descuento(self, carrito, descuentos_previos=0):
        precios = []
        for comensal in carrito.comensales:
            if (comensal.tiene_oferta(self.clave)
                    and comensal.pizza is not None
                    and comensal.pizza.nombre in data.PIZZAS_2X1):
                precios.append(comensal.pizza.precio)
        precios.sort()
        descuento = 0.0
        for i in range(len(precios) // 2):
            descuento += precios[i]
        return round(descuento, 2)


class OfertaMenu(Oferta):
    """Descuento fijo por cada comensal con una pizza y una bebida de menú."""

    clave = "menu"
    nombre = "Menú pizza + bebida"

    def descripcion(self):
        return f"Menú pizza + bebida: {data.DESCUENTO_MENU:.2f} € de descuento por menú (sin IVA)"

    def calcular_descuento(self, carrito, descuentos_previos=0):
        cantidad_menus = 0
        for comensal in carrito.comensales:
            if (comensal.tiene_oferta(self.clave)
                    and comensal.pizza is not None
                    and comensal.bebida is not None):
                cantidad_menus += 1
        return cantidad_menus * data.DESCUENTO_MENU


class OfertaVolumen(Oferta):
    """Porcentaje de descuento cuando el pedido llega al mínimo establecido."""

    clave = "volumen"

    def __init__(self):
        self.nombre = f"Descuento {data.PORCENTAJE_DESCUENTO_VOLUMEN * 100:.0f}% pedido grande"

    def descripcion(self):
        return (f"{data.PORCENTAJE_DESCUENTO_VOLUMEN * 100:.0f}% de descuento si el pedido llega a "
                f"{data.LIMITE_DESCUENTO_VOLUMEN:.0f} € (sin IVA)")

    def alcanza_minimo(self, carrito):
        return carrito.subtotal() >= data.LIMITE_DESCUENTO_VOLUMEN

    def calcular_descuento(self, carrito, descuentos_previos=0):
        if self.alcanza_minimo(carrito):
            base_descuento = max(0, carrito.subtotal() - descuentos_previos)
            return round(base_descuento * data.PORCENTAJE_DESCUENTO_VOLUMEN, 2)
        return 0.0
