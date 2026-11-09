# Pizzería OIA

Aplicación sencilla de consola para tomar pedidos de pizzas y bebidas, calcular el precio y aplicar ofertas.

## Sistema de Autenticación (Login)

Antes de acceder al menú principal de la pizzería, el sistema requiere un inicio de sesión seguro gestionado a través de `login.py`.

- **Validación de Correo:** Se comprueba que el formato sea válido mediante expresiones regulares (ej. `usuario@dominio.com`).
- **Validación de Contraseña:** La clave debe cumplir estrictamente con los siguientes requisitos:
  - Mínimo de 8 caracteres.
  - Al menos una letra minúscula y una letra mayúscula.
  - Al menos un carácter especial[cite: 8].
- **Bucle de Reintentos y Salida:** Si los datos son incorrectos o el formato falla, el sistema permite reintentar de manera indefinida. Se puede salir del programa en cualquier momento escribiendo `exit`[cite: 8].


## Cómo ejecutar

Hay dos métodos que hacen lo mismo (mismo pedido, mismas ofertas, mismo ticket):

- **Método 1 – procedural:** bucles y funciones (`src/metodo_procedural.py`).
- **Método 2 – POO:** clases, objetos y herencia (`src/metodo_oop.py` y `src/clases/`).

Desde la carpeta del proyecto, ejecuta:

```
python main.py                 # menú para elegir el método
python main.py procedural      # método 1 directamente (también: python main.py 1)
python main.py oop             # método 2 directamente (también: python main.py 2)
```

También se puede lanzar cada método por separado:

```
python -m src.metodo_procedural
python -m src.metodo_oop
```

Requiere Python 3.10 o superior (se usa `match`) y no necesita librerías externas.

## Cómo hacer un pedido

1. Cada comensal elige una oferta o la opción **4. Continuar sin oferta**.
2. Elige una pizza de la lista.
3. Puede añadir una bebida.
4. Indica si quiere añadir otro comensal.
5. Al terminar, se muestra el ticket con los productos, el descuento, el IVA y el total.

## Ofertas

- **2x1:** por cada dos pizzas promocionadas, la más barata sale gratis. Las pizzas incluidas son Margarita, Pepperoni y Hawaiana.
- **Menú:** descuenta 1 € por comensal que elija esta oferta y añada una pizza y una bebida.
- **10%:** descuenta el 10% cuando el pedido llega a 30 €. Si se elige esta oferta y aún no se llega al mínimo, hay que añadir otro comensal para continuar.

Las ofertas se pueden elegir por comensal. El resumen final muestra los descuentos que se hayan podido aplicar.

## Modo con clases y objetos

La versión orientada a objetos está en `src/clases/` y reutiliza los datos de `data/data.py`:

- `productos.py`: `Producto`, y sus subclases `Pizza` (calcula su precio a partir de los ingredientes y los costes) y `Bebida`.
- `carta.py`: `Carta`, crea las pizzas y bebidas y permite buscarlas por nombre.
- `carrito.py`: `Comensal` (pizza, bebida y oferta) y `Carrito` (subtotal y ticket).
- `ofertas.py`: clase base `Oferta` con las subclases `Oferta2x1`, `OfertaMenu` y `OfertaVolumen`, y `GestorOfertas` para mostrarlas y aplicarlas.
- `pizzeria.py`: `Pizzeria`, calcula los costes según la temporada y toma el pedido.

Para lanzarlo desde otro archivo:

```
from src.metodo_oop import ejecutar_metodo_2
ejecutar_metodo_2()
```

O directamente:

```
python -m src.metodo_oop
```