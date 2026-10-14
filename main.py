#Archivo Main 
from src.functions import obtener_pizzas_estimadas
from src.functions import obtener_temporada, obtener_pizzas_estimadas
from data import data


#Funcion Temporada


temporada = obtener_temporada()
pizzas_estimadas_mes = obtener_pizzas_estimadas(temporada)
print(pizzas_estimadas_mes)

carrito_pizzas = []
    
def mostrar_carrito(carrito):
    total = 0
    for pizza in carrito:
        total += pizza["precio"]
        output += f"{pizza['nombre']} - ${pizza['precio']:.2f}\n"
    output += f"Total: ${total:.2f}\n"
    return output

booleano = True
while booleano:
    print("Que pizzas quieres comprar? \n")

    data.mostrar_pizzas()

    input_pizza = input("\nIntroduce el nombre de la pizza (o 'salir' para terminar): \n> ")

    if input_pizza.lower() == "salir":
        booleano = False
    elif input_pizza in data.pizzas:
        carrito_pizzas.append(data.pizzas[input_pizza])
    else:
        print("No se ha encontrado pizza, vuelve a introducirla \n> ")


    mostrar_carrito(carrito_pizzas)

