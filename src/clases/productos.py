from data import data


class Producto:
    """Producto genérico de la carta con nombre y precio (sin IVA)."""

    tipo = "producto"

    def __init__(self, nombre, precio=0.0):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: {self.precio:.2f} €"


class Pizza(Producto):
    """Pizza con su lista de ingredientes; el precio se calcula a partir de los costes."""

    tipo = "pizza"

    def __init__(self, nombre, ingredientes):
        super().__init__(nombre)
        self.ingredientes = ingredientes

    def coste_ingredientes(self):
        """Suma de los costes de los ingredientes de la pizza."""
        coste = 0.0
        for ingrediente in self.ingredientes:
            if ingrediente in data.ingredientes:
                coste += data.ingredientes[ingrediente] * data.kg_por_ingrediente
        return coste

    def calcular_precio(self, coste_fijo_por_pizza):
        """Precio de venta: (ingredientes + suministros + coste fijo) * margen."""
        coste_total = self.coste_ingredientes() + data.gasto_suministros_por_pizza + coste_fijo_por_pizza
        return coste_total * data.margen_beneficio

    def descripcion(self):
        return f"{self.nombre}: {', '.join(self.ingredientes)}"


class Bebida(Producto):
    """Bebida de la carta con precio fijo."""

    tipo = "bebida"
