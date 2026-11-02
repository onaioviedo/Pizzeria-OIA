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

def ejecutar_metodo_1():
    print("\n=== EJECUTANDO MÉTODO 1 (PROCEDIMENTAL) ===")
    temporada = obtener_temporada()
    pizzas_estimadas_mes = data.TEMPORADAS_VENTAS[temporada]
    coste_fijo_por_pizza = (data.gasto_personal_mensual + data.gasto_alquiler_mensual) / pizzas_estimadas_mes

    carrito = []
    ofertas_elegidas = []
    numero_comensal = 1
    continuar = True

    while continuar:
        print(f"\n--- COMENSAL {numero_comensal} ---")
        mostrar_ofertas()

        opciones = {"1": "2x1", "2": "menu", "3": "volumen", "4": None}
        while True:
            opcion = input("Elige una opción (1-4): ").strip()
            if opcion in opciones:
                break
            print("Opción no válida. Elige un número del 1 al 4.")

        oferta = opciones[opcion]
        if oferta and oferta not in ofertas_elegidas:
            ofertas_elegidas.append(oferta)

        print("\nPizzas disponibles:")
        data.mostrar_pizzas()
        while True:
            nombre_pizza = input("Elige una pizza: ").strip()
            nombre = None
            for pizza in data.pizzas:
                if pizza.lower() == nombre_pizza.lower():
                    nombre = pizza
                    break
            if nombre is not None:
                break
            print("No se ha encontrado esa pizza, vuelve a introducirla.")

        if oferta == "2x1" and nombre not in data.PIZZAS_2X1:
            print(f"La pizza {nombre} no está incluida en la oferta 2x1.")

        # Opcional: aquí puedes usar tu propia función calcular_coste_ingredientes(data.pizzas[nombre])
        coste_ingredientes = 0
        for ingrediente in data.pizzas[nombre]:
            coste_ingredientes += data.ingredientes[ingrediente] * data.kg_por_ingrediente
            
        coste_total = coste_ingredientes + data.gasto_suministros_por_pizza + coste_fijo_por_pizza
        precio_pizza = coste_total * data.margen_beneficio
        carrito.append({
            "nombre": nombre,
            "precio": precio_pizza,
            "tipo": "pizza",
            "oferta": oferta,
            "comensal": numero_comensal,
        })

        respuesta_bebida = input("¿Quieres añadir una bebida? (s/n): ").strip().lower()
        if respuesta_bebida in ("s", "si", "sí"):
            print("Bebidas disponibles: " + ", ".join(data.BEBIDAS))
            while True:
                nombre_bebida = input("Elige una bebida: ").strip().lower()
                if nombre_bebida in data.BEBIDAS:
                    break
                print("No se ha encontrado esa bebida, vuelve a introducirla.")
            carrito.append({
                "nombre": nombre_bebida.title(),
                "precio": data.BEBIDAS[nombre_bebida],
                "tipo": "bebida",
                "oferta": oferta,
                "comensal": numero_comensal,
            })
        elif oferta == "menu":
            print("La oferta de menú necesita una pizza y una bebida; no se aplicará a este comensal.")

        total_pedido = sum(producto["precio"] for producto in carrito)
        if "volumen" in ofertas_elegidas and total_pedido < data.LIMITE_DESCUENTO_VOLUMEN:
            print(f"Para finalizar con la oferta del 10%, el pedido debe llegar a {data.LIMITE_DESCUENTO_VOLUMEN:.2f} €. Añade otro comensal.")
            numero_comensal += 1
            continue

        respuesta_comensal = input("¿Quieres añadir otro comensal? (s/n): ").strip().lower()
        if respuesta_comensal not in ("s", "si", "sí"):
            continuar = False
        numero_comensal += 1

    descuentos = aplicar_oferta(carrito, ofertas_elegidas)

    if "2x1" in ofertas_elegidas and not any(texto == "Oferta 2x1" for texto, importe in descuentos):
        print("El 2x1 requiere dos pizzas promocionadas: Margarita, Pepperoni o Hawaiana.")

    print("\n--- RESUMEN FINAL ---")
    print(mostrar_carrito(carrito, data.iva, descuentos))

