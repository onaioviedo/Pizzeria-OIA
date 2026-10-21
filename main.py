# Archivo principal
from src.functions import obtener_temporada, mostrar_carrito, mostrar_ofertas, aplicar_oferta
from data import data


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
