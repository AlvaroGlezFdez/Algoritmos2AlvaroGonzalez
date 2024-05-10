import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""

        discounted_price = price * (1 - discount)
        return discounted_price

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        taxed_price = price * (1 + tax_rate)
        return taxed_price

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.


# Creamos los objetos parciales. Para ello fijamos un parámetri de las funciones.
# En caso del primero, fijamos el descuento en un 10% y en caso del segundo fijamos el impuesto en un 21% 

discount_10_percent = functools.partial(operations.apply_discount, discount=0.10)
tax_21_percent = functools.partial(operations.calculate_tax, tax_rate=0.21)
 
# Usar las funciones preconfiguradas.






