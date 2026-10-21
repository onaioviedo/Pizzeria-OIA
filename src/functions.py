from datetime import date

def obtener_temporada(fecha=None):
    """Devuelve 'baja', 'media' o 'alta' según el mes de la fecha."""
    if fecha is None:
        fecha = date.today()

    match fecha.month:
        case 6 | 7 | 8 | 12:        # verano y Navidad
            return "alta"
        case 3 | 4 | 5 | 9 | 10:    # primavera y otoño
            return "media"
        case _:                     # 1, 2, 11
            return "baja"

def obtener_pizzas_estimadas(temporada):
    """Devuelve las pizzas estimadas al mes según la temporada."""
    match temporada.lower():
        case "baja":
            return 600
        case "media":
            return 1000
        case "alta":
            return 1500
        case _:
            return 1000  # valor por defecto si la temporada no es válida

#Funcion costo de ingrediente

def calcular_coste_ingredientes(lista_ingredientes):
    """Calcula la suma de los costes de los ingredientes de una pizza."""
    coste = 0.0
    for ing in lista_ingredientes:
        if ing in INGREDIENTES:
            coste += INGREDIENTES[ing]
    return coste

def mostrar_carrito(carrito, iva):
    base = 0
    output = "Productos:\n"
    for pizza in carrito:
        base += pizza["precio"]
        output += f"- Pizza {pizza['nombre']}: {pizza['precio'] * (1 + iva):.2f} €\n"
    importe_iva = base * iva
    output += f"\nBase imponible: {base:.2f} €\n"
    output += f"IVA: {importe_iva:.2f} €\n"
    output += f"Total: {base + importe_iva:.2f} €\n"
    return output

# Función Ofertas

def oferta_2x1(carrito, pizzas_estimadas):
    """Por cada 2 pizzas de la lista 2x1, la más barata es gratis."""
    precios = []
    for producto in carrito:
        if producto in data.PIZZAS_2X1:
            precios.append(calcular_precio_pizza(producto, pizzas_estimadas))
    precios.sort()
    descuento = 0.0
    for i in range(len(precios) // 2):
        descuento += precios[i]
    return round(descuento, 2)
 
 
def oferta_menu(carrito):
    """Cada pareja pizza + bebida tiene un descuento fijo."""
    num_pizzas = 0
    num_bebidas = 0
    for producto in carrito:
        if producto in data.pizzas:
            num_pizzas += 1
        else:
            num_bebidas += 1
    return min(num_pizzas, num_bebidas) * data.DESCUENTO_MENU
 
 
def oferta_volumen(subtotal):
    """10 % de descuento si el pedido supera el límite."""
    if subtotal > data.LIMITE_DESCUENTO_VOLUMEN:
        return round(subtotal * data.PORCENTAJE_DESCUENTO_VOLUMEN, 2)
    return 0.0
 
 
def aplicar_oferta(carrito, pizzas_estimadas):
    """Devuelve la lista de descuentos aplicados como (texto, importe)."""
    descuentos = []
    subtotal = calcular_total_carrito(carrito, pizzas_estimadas)
 
    d_2x1 = oferta_2x1(carrito, pizzas_estimadas)
    if d_2x1 > 0:
        descuentos.append(("Oferta 2x1", d_2x1))
        subtotal -= d_2x1
 
    d_menu = oferta_menu(carrito)
    if d_menu > 0:
        descuentos.append(("Menú pizza + bebida", d_menu))
        subtotal -= d_menu
 
    d_volumen = oferta_volumen(subtotal)
    if d_volumen > 0:
        descuentos.append((f"Descuento {data.PORCENTAJE_DESCUENTO_VOLUMEN * 100:.0f}% pedido grande", d_volumen))
 
    return descuentos