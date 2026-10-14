#Archivo Main 




#Funcion Temporada
temporada = "media" 
match temporada: 
    case "baja": 
        pizzas_estimadas_mes = 1000 
    case "media": 
        pizzas_estimadas_mes = 1850 
    case "alta": 
        pizzas_estimadas_mes = 3000 
    case _: 
        pizzas_estimadas_mes = 1000
