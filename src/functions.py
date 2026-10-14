
#Funcion costo de ingrediente

def calcular_coste_ingredientes(lista_ingredientes):
    """Calcula la suma de los costes de los ingredientes de una pizza."""
    coste = 0.0
    for ing in lista_ingredientes:
        if ing in INGREDIENTES:
            coste += INGREDIENTES[ing]
    return coste