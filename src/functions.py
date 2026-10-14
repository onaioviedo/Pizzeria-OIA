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
