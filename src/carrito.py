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
