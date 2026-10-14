#Archivo Main
from src.functions import obtener_temporada, obtener_pizzas_estimadas, mostrar_carrito
from data import data

temporada = obtener_temporada()
pizzas_estimadas_mes = obtener_pizzas_estimadas(temporada)
coste_fijo_por_pizza = (data.gasto_personal_mensual + data.gasto_alquiler_mensual) / pizzas_estimadas_mes

carrito_pizzas = []

while True:
    print("\nQue pizzas quieres comprar? \n")
    data.mostrar_pizzas()

    input_pizza = input("\nIntroduce el nombre de la pizza (o 'salir' para terminar): \n> ")

    if input_pizza.lower() == "salir":
        break

    # Buscar la pizza sin distinguir mayúsculas
    nombre = None
    for pizza in data.pizzas:
        if pizza.lower() == input_pizza.strip().lower():
            nombre = pizza

    if nombre is None:
        print("No se ha encontrado la pizza, vuelve a introducirla")
        continue

    # Precio de la pizza: ingredientes (€/kg * kg usados) + suministros + parte de gastos fijos, con margen
    coste_ingredientes = 0
    for ingrediente in data.pizzas[nombre]:
        coste_ingredientes += data.ingredientes[ingrediente] * data.kg_por_ingrediente
    coste_total = coste_ingredientes + data.gasto_suministros_por_pizza + coste_fijo_por_pizza
    precio_sin_iva = coste_total * data.margen_beneficio

#gastos_fijos_mensuales = gasto_personal_mensual + gasto_alquiler_mensual
#coste_fijo_por_pizza = gastos_fijos_mensuales / pizzas_estimadas_mes
#coste_total_pizza = coste_ingredientes + gasto_suministros_por_pizza +
#coste_fijo_por_pizza
#precio_sin_iva = coste_total_pizza * 1.35
#precio_con_iva = precio_sin_iva * (1 + iva)

#TO DO - Merge con main y considerar ofertas y bebidas!!!!

    carrito_pizzas.append({"nombre": nombre, "precio": precio_sin_iva})
    print("\n" + mostrar_carrito(carrito_pizzas, data.iva))
