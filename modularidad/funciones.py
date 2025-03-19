# Definiendo una función
def say_hello():
    print("Hello 👌")


# Invocar una función

say_hello()


# Retornar un valor: Devuelven un valor
def one():
    return 1


result = one()
print(result)

# Podemos asignar la función a una variable
value = one()
print(value)

if one() == 1:
    print("It works")
else:
    print("Something is broken")


# Si una función no incluye 'return' devuelve None
def empty():
    x = 0
    # return None


print(empty())


# return a secas, hace que salgamos de la función
def quick():
    return


print(quick())

"""
Retornando múltiples valores:
"""


def multiple():
    return 0, 1  # is a tuple!


result = multiple()
print(result)
print(type(result))

# Aplicando el desempaquetado de tuplas o destructuración
a, b = multiple()
print(a)
print(b)

"""
Párametros y argumentos: Si una función no dispusiera de valores de entrada, su comportamiento quedaría muy limitado. Es por ello que los parámetros permiten variar los datos que consume una función para obtener distintos resultados.
"""


# Parámetro de la función: value
def sqrt(value):
    return value ** (1 / 2)


# Argumento de la función: 4
print(sqrt(4))


def _min(a, b):
    if a < b:
        return a
    else:
        return b


print(_min(7, 9))


# Teniendo en cuenta que la sentencia return finaliza la ejecución de la función
# es viable eliminar la sentence else
def _SecondMin(a, b):
    if a < b:
        return a
    return b


print(_SecondMin(4, 2))

"""
Argumentos posicionales: Los argumentos posicionales son aquellos argumentos que se copian en sus correspondientes parámetros por orden de escritura.
"""


def build_cpu(vendor, num_cores, freq):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


print(build_cpu("AMD", 8, 2.7))

"""
Argumentos nominales: 
Los argumentos no son copiados en un orden específico sino que se asignan por nombre a cada párametro. Para utilizarlo, basta con realizar la asignación de cada argumento en la propia llamada a la función.
"""
# El orden de los argumentos no influyen en el resultado final.
print(build_cpu(vendor="AMD", num_cores=8, freq=2.7))
print(build_cpu(freq=2.7, vendor="AMD", num_cores=8))

## Se puede mezclar, los posicionales van antes que los nominales
print(build_cpu("INTEL", num_cores=4, freq=3.1))

"""
Argumentos mutables e inmutables:
Cuando realizamos modificaciones a los argumentos de una función es importante tener en cuenta si son mutables (listas, diccionarios, conjuntos, ...) o inmutables (tuplas, enteros, flotantes, cadenas de texto, ...).
"""
values = [2, 3, 4]


def square_it(values):
    # NO HACER ESTO ✖️
    for i in range(len(values)):
        values[i] **= 2
    return values


print(square_it(values))

"""
Parámetros por defecto:
Es posible especificar valores por defecto en los parámetros de una función. En el caso de que no se proporcione un valor al argumento en la llamada a la función, el parámetro correspondiente tomará el valor definido por defecto.
"""


def build_cpu(vendor, num_cores, freq=2.0):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


# Llamada a la función sin especificar el argumento freq
print(build_cpu("INTEL", 2))

# Lllamada a la función especificando el argumento freq
print(build_cpu("INTEL", 2, freq=3.4))

# Los valores por defecto en los parámetros se calculan cuando se define la
# función, no cuando se ejecuta la función

DEFAULT_FREQ = 2.0


def build_cpu(vendor, num_cores, freq=DEFAULT_FREQ):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


print(build_cpu("AMD", 4))

DEFAULT_FREQ = 3.5

print(build_cpu("AMD", 4))

"""
Modificar parámetros mutables:
"""


""" def buggy(arg, result=[]):
    result.append(arg)
    print(result) """


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy("a")
nonbuggy("b")
nonbuggy("a", ["x", "y", "z"])
nonbuggy("b", ["x", "y", "z"])

"""
Empaquetar / Desempaquetar argumentos:
"""

values = (4, 3, 2, 1)


# Empaquetar argumentos posicionales: *
def _sum(*values):
    print(f"{values=}")
    result = 0
    for value in values:
        result += value
    return result


print(_sum(4, 3, 2, 1))

# Desempaquetar argumentos posicionales: *
print(_sum(*values))

"""
Empaquetar / Desempaquetar argumentos: Parámetros nominales
"""

marks = {"ana": 8, "antonio": 6, "inma": 9, "javier": 7}


# Empaquetar argumentos nominales:  **
def best_student(**marks):
    print(f"{marks=}")
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student


best_student(ana=8, antonio=6, inma=9, javier=7)

# Desempaquetar argumentos nominales:  **
best_student(**marks)

"""
CONVENCIONES: 
En muchas ocasiones se utiliza args como nombre de parámetro para argumentos posicionales y kwargs como nombre de parámetro para argumentos nominales.
"""


def func(*args, **kwargs):
    # TODO
    pass


"""
Forzado modo de paso de argumentos:
"""


# Argumentos sólo nominales: La definición de los parámetros de la función sean
# pasados sólo por nombre
def sum_power(a, b, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(sum_power(3, 4))
print(sum_power(a=3, b=4))
print(sum_power(3, 4, power=True))

# Argumentos solo posicionales: Obligar a que determinados parámetros sean
# pasados por posición
# / : Separador para específicar que parámetros posicionales.


def sum_power(a, b, /, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


result1 = sum_power(3, 4)
result2 = sum_power(3, 4, power=True)
result3 = sum_power(3, 4, True)

print(result1)
print(result2)
print(result3)

"""
Fijando argumentos posicionales y nominales:

Podemos forzar a que una función reciba argumentos de un modo concreto.
"""


def sum_power(a, b, /, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(sum_power(3, 2, power=True))

"""
Funciones como parámetros:
Las funciones se pueden utilzar en cualquier contexto del programa. Son objetos que pueden ser asignados a variables, usados en expresiones, devueltos como valores de retorno o pasados como argumentos a otras funciones.
"""


def success():
    print("Yeah!")


print(type(success))


def doit(fn):
    fn()


# Pasando funcines como argumentos
doit(success)


def repeat_please(text, time=1):
    return text * time


print(type(repeat_please))


def second_doit(fn, arg1, arg2):
    return fn(arg1, arg2)


print(second_doit(repeat_please, "Function as params ", 4))

"""
DOCUMENTACIÓN:
"""


def sqrt(value):
    "Return the square root of the value."
    return value ** (1 / 2)


# La forma más ortodoxa de escribir un docstring es con triple comillas


def closest_int(value):
    """Returns the closest integer to the given value.
    The operation is:
        1. Compute distance to floor.
        2. If distance less than a half, return floor.
           Otherwise, return ceil.
    """
    floor = int(value)
    if value - floor < 0.5:
        return floor
    else:
        return floor + 1


# Para ver el docstring de una función, basta con utilizar help()
help(closest_int)

# Extraer información usando el símbolo ?

# closest_int?

"""
Anotación de tipos: Las anotaciones de tipo o type-hints permiten indicar tipos para los parámetros de una función y/o para su valor de retorno (también funciona para variables).
"""


def ssplit(text: str, split_pos: int) -> tuple:
    return text[:split_pos], text[split_pos:]


print(ssplit("Always remember us this way", 15))

"""
Valores por defecto:
"""
