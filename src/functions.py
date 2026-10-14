
#Funcion costo de ingrediente
import datos

def calcular_coste_ingredientes(lista_ingredientes):
    """Calcula la suma de los costes de los ingredientes de una pizza."""
    coste = 0.0
    for ing in lista_ingredientes:
        if ing in INGREDIENTES:
            coste += INGREDIENTES[ing]
    return coste

#función para calcular el PVP final de la bebida

def calcular_precio_bebida(nombre_bebida: str) -> float:
    """Calcula el precio de venta al público a partir del coste de compra y el margen comercial."""
    coste = datos.coste_bebidas[nombre_bebida]
    precio_sin_iva = coste * (1 + datos.margen_bebida)
    precio_con_iva = precio_sin_iva * (1 + datos.iva)
    return round(precio_con_iva, 2)

# Función para analizar qué productos hay en el carrito y calcula cuánto dinero se descuenta.

def aplicar_ofertas(carrito: list, temporada: str = "media") -> tuple[float, list[str]]:
    """
    Evalúa las 3 ofertas mínimas requeridas:
    1. 2x1 en pizzas Margarita.
    2. Menú (Pizza + Bebida).
    3. Descuento del 10% si el pedido supera 30€.
    """
    descuentos_aplicados = []
    descuento_total = 0.0

    # Separamos pizzas y bebidas que están en el carrito
    pizzas_en_carrito = [item for item in carrito if item in datos.pizzas]
    bebidas_en_carrito = [item for item in carrito if item in datos.bebidas]

    # --- OFERTA 1: 2x1 en Margarita ---
    margaritas = pizzas_en_carrito.count("Margarita")
    margaritas_gratis = margaritas // 2
    if margaritas_gratis > 0:
        precio_margarita = calcular_precio_pizza("Margarita", temporada)["precio_con_iva"]
        ahorro_2x1 = margaritas_gratis * precio_margarita
        descuento_total += ahorro_2x1
        descuentos_aplicados.append(f"Promo 2x1 en Margarita ({margaritas_gratis} gratis): -{ahorro_2x1:.2f}€")

    # --- OFERTA 2: Menú Pizza + Bebida ---
    pizzas_para_combo = len(pizzas_en_carrito) - margaritas_gratis
    num_combos = min(pizzas_para_combo, len(bebidas_en_carrito))
    if num_combos > 0:
        ahorro_combo = num_combos * 0.80  # Descuento fijo por cada combinación
        descuento_total += ahorro_combo
        descuentos_aplicados.append(f"Promo Menú Pizza + Bebida (x{num_combos}): -{ahorro_combo:.2f}€")

    # --- OFERTA 3: 10% de descuento si supera 30€ ---
    # (Se calcula sobre el subtotal que queda tras las anteriores)
    
    return round(descuento_total, 2), descuentos_aplicados

