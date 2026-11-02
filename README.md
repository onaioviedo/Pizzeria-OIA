# Pizzería OIA

Aplicación sencilla de consola para tomar pedidos de pizzas y bebidas, calcular el precio y aplicar ofertas.

## Cómo ejecutar

Desde la carpeta del proyecto, ejecuta:

```bash
python main.py
```

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

```python
from src.clases.pizzeria import ejecutar
ejecutar()
```

O directamente:

```bash
python -m src.clases.pizzeria
```
