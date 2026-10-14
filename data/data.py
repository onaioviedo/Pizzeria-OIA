#Base de datos

#Gastos fijos
GASTO_PERSONAL_MENSUAL = 4200.0
GASTO_ALQUILER_MENSUAL = 1600.0
GASTO_SUMINISTROS_POR_PIZZA = 0.60
IVA = 0.10  # 10%

#Estimación de ventas mensuales por temporada
TEMPORADAS_VENTAS = {
    "baja": 1000,
    "media": 1850,
    "alta": 3000}

#Carta de bebidas
BEBIDAS = {
    "agua": 1.20,
    "cola": 2.00,
    "limonada": 2.00,
    "cerveza": 2.50}

# Precios de los ingredientes (€/kg)
ingredientes = {
    "harina": 1.20,           # Harina de fuerza / trigo para pizza
    "tomate": 1.60,           # Salsa de tomate triturado / passata
    "queso": 7.50,            # Queso rallado mezcla / gouda
    "mozzarella": 8.20,       # Mozzarella rallada / fior di latte
    "jamon": 7.90,            # Jamón cocido / york en dados o lonchas
    "bacon": 8.50,            # Bacon ahumado en tiras
    "pollo": 6.80,            # Pechuga de pollo cocinada / marinada
    "atun": 9.50,             # Atún claro en conserva escurrido
    "champinones": 3.40,      # Champiñón fresco laminado
    "cebolla": 1.30,          # Cebolla morada o dulce en juliana
    "aceitunas": 4.50,        # Aceitunas negras / verdes deshuesadas
    "pepperoni": 11.20,       # Pepperoni / salami especiado en rodajas
    "pimenton": 4.20,         # Pimiento rojo fresco en tiras

    # Ingredientes añadidos para complementar la carta
    "carne_picada": 7.40,     # Carne picada de vacuno/cerdo salteada
    "pina": 2.10,             # Piña troceada escurrida
    "anchoas": 18.50,         # Filetes de anchoa en aceite
    "gorgonzola": 12.80,      # Queso azul / gorgonzola
    "parmesano": 15.60,       # Queso parmesano curado rallado / lascas
    "salsa_barbacoa": 3.80,   # Salsa barbacoa para pizza
    "jalapenos": 5.20,        # Jalapeños encurtidos en rodajas
    "rucula": 9.80,           # Rúcula fresca seleccionada
    "albahaca": 14.00,        # Albahaca fresca
    "oregano": 12.00,         # Orégano seco molido
}

# Gastos fijos y variables
gasto_suministros_por_pizza = 0.60
gasto_personal_mensual = 4200
gasto_alquiler_mensual = 1600
iva = 0.10
margen_beneficio = 1.35         # 35 % sobre el coste total
kg_por_ingrediente = 0.08       # los precios son €/kg: se usan 80 g de cada ingrediente por pizza

# Tipos de pizza y sus ingredientes
pizzas = {
    # 1. Clásica básica
    "Margarita": ["harina", "tomate", "mozzarella", "albahaca"],
    # 2. Clásica con jamón
    "Prosciutto": ["harina", "tomate", "queso", "jamon", "oregano"],
    # 3. La tradicional barbacoa
    "Barbacoa": ["harina", "tomate", "queso", "bacon", "pollo", "carne_picada", "salsa_barbacoa"],
    # 4. Clásica con pepperoni
    "Pepperoni": ["harina", "tomate", "mozzarella", "pepperoni", "oregano"],
    # 5. La clásica combinación dulce y salada
    "Hawaiana": ["harina", "tomate", "mozzarella", "jamon", "pina"],
    # 6. Variedad con champiñón y jamón
    "Capricciosa": ["harina", "tomate", "mozzarella", "jamon", "champinones", "aceitunas"],
    # 7. Selección de quesos
    "Cuatro_Quesos": ["harina", "tomate", "mozzarella", "queso", "gorgonzola", "parmesano"],
    # 8. Sabor marinero
    "Marinara_Especial": ["harina", "tomate", "mozzarella", "atun", "cebolla", "aceitunas"],
    # 9. Con anchoas tradicional
    "Napolitana": ["harina", "tomate", "mozzarella", "anchoas", "aceitunas", "oregano"],
    # 10. Pizza de huerto
    "Vegetal": ["harina", "tomate", "mozzarella", "champinones", "cebolla", "pimenton", "aceitunas"],
    # 11. Con pollo y verdura
    "Pollo_Grill": ["harina", "tomate", "queso", "pollo", "pimenton", "cebolla"],
    # 12. Estilo tex-mex picante
    "Diabla": ["harina", "tomate", "mozzarella", "pepperoni", "carne_picada", "jalapenos"],
    # 13. Toque crujiente y ahumado
    "Carbonara_Pizza": ["harina", "queso", "mozzarella", "bacon", "cebolla", "champinones"],
    # 14. Pollo barbacoa dulce
    "Pollo_BBQ": ["harina", "mozzarella", "pollo", "bacon", "cebolla", "salsa_barbacoa"],
    # 15. Pizza con carnes y toque fresco
    "Boloñesa_Rústica": ["harina", "tomate", "queso", "carne_picada", "parmesano", "oregano"],
    # 16. Pizza fresca y gourmet
    "Rúcula_y_Parmesano": ["harina", "tomate", "mozzarella", "rucula", "parmesano"],
    # 17. Fuerte y con carácter
    "Gorgonzola_y_Bacon": ["harina", "mozzarella", "gorgonzola", "bacon", "cebolla"],
    # 18. Fusión atún y bacon
    "Atún_Especial": ["harina", "tomate", "queso", "atun", "bacon", "pimenton", "aceitunas"],
    # 19. Explosiva con jalapeño
    "Mexicana_Pollo": ["harina", "tomate", "queso", "pollo", "jalapenos", "pimenton", "cebolla"],
    # 20. Gran carnívora
    "Carnívora_Suprema": ["harina", "tomate", "mozzarella", "jamon", "bacon", "pepperoni", "carne_picada"],
}

# Ejemplo de uso
def mostrar_pizzas():
    for nombre, ingredientes in pizzas.items():
        print(f"{nombre}: {', '.join(ingredientes)}")