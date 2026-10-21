from datetime import date
from data import data

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
        if ing in data.ingredientes:
            coste += data.ingredientes[ing] * data.kg_por_ingrediente
    return coste

# Funcion mostrar carrito de oferta

def mostrar_carrito(carrito, iva, descuentos=None):
    """Ticket: productos, descuentos de ofertas, base, IVA y total."""
    if descuentos is None:
        descuentos = []
    subtotal = 0
    output = "Productos:\n"
    for producto in carrito:
        subtotal += producto["precio"]
        output += f"- {producto['nombre']}: {producto['precio']:.2f} €\n"

    total_descuentos = 0
    if len(descuentos) > 0:
        output += "\nDescuentos:\n"
        for texto, importe in descuentos:
            total_descuentos += importe
            output += f"- {texto}: -{importe:.2f} €\n"

    base = subtotal - total_descuentos
    importe_iva = base * iva
    output += f"\nDescuento total: {total_descuentos:.2f} €\n"
    output += f"\nBase imponible: {base:.2f} €\n"
    output += f"IVA: {importe_iva:.2f} €\n"
    output += f"Total: {base + importe_iva:.2f} €\n"
    return output

# Función Ofertas

def mostrar_ofertas():
    """Muestra las ofertas disponibles."""
    print("\n--- OFERTAS ---")
    print(f"1. 2x1 por cada 2 pizzas de: {', '.join(data.PIZZAS_2X1)}")
    print(f"2. Menú pizza + bebida: {data.DESCUENTO_MENU:.2f} € de descuento por menú (sin IVA)")
    print(f"3. {data.PORCENTAJE_DESCUENTO_VOLUMEN * 100:.0f}% de descuento si el pedido llega a "
          f"{data.LIMITE_DESCUENTO_VOLUMEN:.0f} € (sin IVA)")
    print("4. Continuar sin oferta")


def pedir_ofertas():
    """Pide los números de las ofertas que se quieren aplicar."""
    texto = input("Elige ofertas por número, separadas por comas (Enter = ninguna): ")
    claves = {"1": "2x1", "2": "menu", "3": "volumen"}
    elegidas = []
    for numero in texto.split(","):
        numero = numero.strip()
        if numero in claves and claves[numero] not in elegidas:
            elegidas.append(claves[numero])
    return elegidas


def oferta_2x1(carrito):
    """Por cada 2 pizzas de la lista 2x1, la más barata es gratis."""
    precios = []
    for producto in carrito:
        if (producto["tipo"] == "pizza"
                and producto.get("oferta") == "2x1"
                and producto["nombre"] in data.PIZZAS_2X1):
            precios.append(producto["precio"])
    precios.sort()
    descuento = 0.0
    for i in range(len(precios) // 2):
        descuento += precios[i]
    return round(descuento, 2)


def oferta_menu(carrito):
    """Aplica un descuento por comensal con una pizza y una bebida de menú."""
    comensales = {}
    for producto in carrito:
        if producto.get("oferta") == "menu":
            numero = producto.get("comensal")
            if numero not in comensales:
                comensales[numero] = {"pizza": 0, "bebida": 0}
            if producto.get("tipo") in comensales[numero]:
                comensales[numero][producto["tipo"]] += 1

    cantidad_menus = 0
    for productos in comensales.values():
        if productos["pizza"] == 1 and productos["bebida"] == 1:
            cantidad_menus += 1
    return cantidad_menus * data.DESCUENTO_MENU


def oferta_volumen(subtotal, descuentos_previos=0):
    """10 % de descuento cuando el pedido llega al mínimo establecido."""
    if subtotal >= data.LIMITE_DESCUENTO_VOLUMEN:
        base_descuento = max(0, subtotal - descuentos_previos)
        return round(base_descuento * data.PORCENTAJE_DESCUENTO_VOLUMEN, 2)
    return 0.0


def aplicar_oferta(carrito, ofertas_elegidas):
    """Devuelve la lista de descuentos de las ofertas elegidas como (texto, importe)."""
    descuentos = []
    subtotal = 0
    for producto in carrito:
        subtotal += producto["precio"]

    if "2x1" in ofertas_elegidas:
        d_2x1 = oferta_2x1(carrito)
        if d_2x1 > 0:
            descuentos.append(("Oferta 2x1", d_2x1))
            subtotal -= d_2x1

    if "menu" in ofertas_elegidas:
        d_menu = oferta_menu(carrito)
        if d_menu > 0:
            descuentos.append(("Menú pizza + bebida", d_menu))
            subtotal -= d_menu

    if "volumen" in ofertas_elegidas:
        subtotal_bruto = sum(producto["precio"] for producto in carrito)
        descuentos_previos = sum(importe for texto, importe in descuentos)
        d_volumen = oferta_volumen(subtotal_bruto, descuentos_previos)
        if d_volumen > 0:
            descuentos.append((f"Descuento {data.PORCENTAJE_DESCUENTO_VOLUMEN * 100:.0f}% pedido grande", d_volumen))

    return descuentos

