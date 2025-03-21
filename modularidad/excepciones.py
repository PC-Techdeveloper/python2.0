"""
Excepciones:
Una excepción es el bloque de código que se lanza cuando se produce un error en la ejecución de un programa en Python.
"""


# Manejo de errores:
def int_div(a: int, b: int) -> int:
    try:
        return a // b
    except:
        print("Please do not divide by zero...")


print(int_div(3, 2))

"""
Especificando excepciones:
1. TypeError: Por si los operadores no permiten la división.
2. ZeroDivisionError: Por si el denominador es cero.
3. Exception: Para cualquier otro error que se pueda producir.
"""


def intDiv(a: int, b: int) -> int:
    try:
        result = a // b
    except TypeError:
        print("Checks operands. Some of them seems strange...")
    except ZeroDivisionError:
        print("You can't divide by zero...")
    except Exception:
        print("Something went wrong...")


intDiv(3, 0)
intDiv(3, "0")

"""
Excepciones predefinidas:

AttributeError:

Referencia de atributo inexistente

'hello'.splik():

IndexError:

Subíndice de secuencia fuera de rango

(2, 3)[5]

KeyError:

Clave de diccionario no encontrada

{0:1, 1:2}[2]

NotImplementedError:

La operación debe ser implementada

OSError:

Error al usar una función del sistema operativo (E/S)

open('null.txt')

RecursionError:

Alcanzado el máximo nivel de recursión

StopIteration:

Fin del protocolo de iteración

TypeError:

Operación sobre un objeto de tipo inapropiado

'x' / 3

ValueError:

Operación sobre un objeto de tipo correcto pero valor inapropiado

int('x')

ZeroDivisionError:

Segundo argumento de división o módulo es cero

1 / 0
"""

## Agrupando excepciones


def intDivision(a: int, b: int) -> int:
    try:
        result = a // b
    except (TypeError, ZeroDivisionError):
        print("Checks the operands ✖️")
    except Exception:
        print("Something went wrong... ⚠️")


intDivision(3, 0)

"""
Variantes:

Python proporciona la cláusula else para saber que todo ha ido bien y que no se ha lanzado ninguna excepción. Esto es relevante a la hora de manejar los errores.

De igual modo, tenemos a nuestra disposición la cláusula finally que se ejecuta siempre, independientemente de si ha habido o no ha habido error.
"""

values = [4, 2, 7]

try:
    r = values[3]
except IndexError:
    print("Index not in list ✖️")
else:
    print(f"Your wishes are my commandments {r}")
finally:
    print("Always do this ✅")

try:
    r = values[2]
except IndexError:
    print("Error: Index not in list ❌")
else:
    print(f"Your wishes are my command: {r}")
finally:
    print("Have a good day! 🌄")

"""
Mostrando los errores:

Para ello hacer uso de la palabra reservada 'as' junto al nombre de la variable que contiene el error.
"""

try:
    print(values[3])
except IndexError as err:
    # print(err)  # Muestra el error
    print(f"Something went wrong: {err}")

"""
Elevando excepciones:
Dar uso de la palabra reservada 'raise' para elevar o levantar una excepción.
"""


def _sum(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError("Operands must be integers")


_sum(3, 4)  # Todo normal
# _sum("x", "y")

"""
Excepciones personalizadas/propias:
"""


class NotIntError(Exception):
    pass


values = (4, 7, 2.11, 9)

""" for value in values:
    if not isinstance(value, int):
        raise NotIntError(value)
"""

"""
Mensajes personalizados:
Podemos personalizar la excepción propia añadiendo un mensaje como valor por defecto.
"""


""" class SecondNotIntError(Exception):
    def __init__(self, message="This module only works with integers. Sorry ❌"):
        super().__init__(message)


raise SecondNotIntError() """

# Incorporando en el mensaje de la excepción el propio valor que está generando
# el error.


""" class NotIntError(Exception):
    def __init__(
        self, value, *, message="This module only works with integers. Sorry!"
    ):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.value} -> {self.message}"

# Modificando el mensaje de la excepción
raise NotIntError(3.14, message="Please use integers only ⚠️")
"""

"""
Aserciones: Permite comprobar si se están cumpliendo las expectativas del programa y en caso contrario, lanza una excepción informativa.
"""

result = 10

assert result > 0

print(result)

result2 = -1
# Añadir un mensaje personalizado informativo como segundo parámetro
assert result2 > 0, "Negative numbers are not allowed ❌"

print(result2)
