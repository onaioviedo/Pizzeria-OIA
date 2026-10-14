#Archivo Main 
from src.functions import obtener_pizzas_estimadas
from src.functions import obtener_temporada, obtener_pizzas_estimadas


#Funcion Temporada


temporada = obtener_temporada()
pizzas_estimadas_mes = obtener_pizzas_estimadas(temporada)
print(pizzas_estimadas_mes)
