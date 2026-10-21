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
