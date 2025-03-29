# Definiendo una función
from functools import reduce


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

# Se puede mezclar, los posicionales van antes que los nominales
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
Valores por defecto: Cuando usamos anotaciones de tipos también podemos indicar un valor por defecto para los parámetros.

Las anotaciones de tipos son una herramienta muy potente, permite complementar la documentación de nuestro código y aclarar ciertos aspectos. 
"""


def ssplit(text: str, split_pos: int = -1) -> tuple:
    if split_pos == -1:
        split_pos = len(text)
    return text[:split_pos], text[split_pos:]


print(ssplit("Always remember us this way"))

"""
Número indefinido:
Cuando trabajamos con parámetros que representan un número indefinido de valores, las anotaciones de tipo sólo hacen referencia al tipo que contiene la tupla, no es necesario indicar que es una tupla.
"""


def _max(*args: int | float):
    pass


"""
TIPOS DE FUNCIONES: 
Funciones lambda: Las funciones lambda son funciones anónimas que se definen en una sola línea. Se utilizan para crear funciones pequeñas y simples de forma rápida y concisa.
"""


def num_words(t): return len(t.split())


print(type(num_words))
print(num_words)
print(num_words("Hi my friend, how are you? 🖐️"))


def logic_and(x, y): return x & y


for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {logic_and(i, j)}")

# Lambdas como argumentos

geoloc = (
    (15.623037, 13.258358),
    (55.147488, -2.667338),
    (54.572062, -73.285171),
    (3.152857, 115.327724),
    (-40.454262, 172.318877),
)

print(sorted(geoloc))

print(sorted(geoloc, key=lambda t: t[1]))

"""
Enfoque funcional: El enfoque funcional es un paradigma de programación que se basa en el uso de funciones puras y evita el uso de efectos secundarios. En este enfoque, las funciones son tratadas como ciudadanos de primera clase y se pueden pasar como argumentos, devolver como valores y almacenar en variables.
"""

# map(): Devuelve un generador, por lo tanto hay que convertirlo
# a una lista o iterable para ver los resultados.
# Aplica otra función sobre cada elemento de un iterable.


def f(x):
    return x**2 / 2


data = range(1, 11)

map_gen = map(f, data)
print(type(map_gen))

print(f"map:", list(map_gen))

# Mismo resultado aplicando una función anónima

print(list(map(lambda x: x**2 / 2, data)))

# Mismo resultado aplicando una lista por comprensión
print([x**2 / 2 for x in data])

# filter(): Selecciona aquellos elementos de un iterable que cumplen
# una determinada condición.
# también devuelve un generador, por lo tanto hay que convertirlo
# a una lista o iterable para ver los resultados.


def odd_number(x: int) -> int:
    return x % 2 == 1


data2 = range(1, 21)

filter_gen = filter(odd_number, data2)

print(type(filter_gen))

print(f"filter:", list(filter_gen))

print(list(filter(lambda x: x % 2 == 1, data)))
print([x for x in data if x % 2 == 1])

"""
reduce(): Permite reducir una función sobre un conjunto de valores. 
Para poder usar la función reduce es necesario importar el módulo functools
"""


def mult_values(a, b):
    return a * b


data = range(1, 6)

print(reduce(mult_values, data))

# Aplicando una función lambda
print(reduce(lambda x, y: x * y, data))

"""
GENERADORES:
Un generador se encarga de generar valores que permita tratarlos de manera individual (y aislada). 

Existen dos implementaciones de generadores:
- Funciones generadoras.
- Expresiones generadoras.
"""


# Funciones generadoras: incorporar la sentencia yield
# Devuelve un valor indicado, y a la vez, congela el estado de la función
def evens(lim: int):
    for i in range(0, lim + 1, 2):
        yield i


print(type(evens))

evens_gen = evens(20)  # devuelve un generador.

print(type(evens_gen))

# Una vez creado el generador, ya permite iterar sobre el
for even in evens(20):
    print(even, end=" ")

"""
Expresiones generadoras:
Una expresión generadora es similar a la lista por comprensión, sólo que se utiliza paréntesis en vez de corchetes.
"""

evens_gen = (i for i in range(0, 20, 2))
print(type(evens_gen))

for i in evens_gen:
    print(i, end=" ")

# Una expresión generadora se puede explicitar
print("---- EXPRESIÓN GENERADORA EXPLICITAMENTE ----")
print(f"LIST:", list(i for i in range(0, 20, 2)))
print(f"SUM:", sum(i for i in range(0, 20, 2)))
print(f"MIN:", min(i for i in range(0, 20, 2)))
print(f"MAX:", max(i for i in range(0, 20, 2)))
print(f"SORTED:", sorted(i for i in range(0, 20, 2)))

"""
Funciones Interiores:
Está permitido definir funciones dentro de otra función. Es lo que se conoce como función interior.
"""


def get_words_with_all_vowels(text: str) -> list[str]:
    VOWELS = "aeiou"

    def get_unique_vowels(word: str) -> set[str]:
        return set(c for c in word if c in VOWELS)

    result = []
    for word in text.split():
        if len(get_unique_vowels(word)) == len(VOWELS):
            result.append(word)
    return result


print(get_words_with_all_vowels("La euforia de ver el riachuelo fue inmensa"))

"""
Clausuras:
Una clausura (closure) establece el uso de una función interior que se genera dinámicamente y recuerda los valores de los argumentos con los que fue creada.

En una clausura retomamos una función, no una llamada a una función. Es por esto que se dice que una clausura es una factoria de funciones.
"""


def make_multiplier_of(n: int):
    def multiplier(x: int) -> int:
        return x * n

    return multiplier


m3 = make_multiplier_of(3)
print(type(m3))
print(m3(7))

m5 = make_multiplier_of(5)
print(type(m5))
print(m5(8))

# Llamada directa
print(make_multiplier_of(10)(11))

"""
Decoradores:
Un decorador es una función que recibe como parámetro una función y devuelve otra función.
"""

# Esqueleto básico de un decorador


def my_decorator(func):  # Nombre del decorador
    def wrapper(*args, **kwargs):  # Función interior
        return func(*args, **kwargs)  # argumentos posicionales y nominales

    return wrapper


def res2bin(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return bin(result)

    return wrapper


# Definiendo una función ordinaria
def power(x: int, n: int) -> int:
    return x**n


print(power(2, 3))
print(power(4, 5))

# Aplicando el decorador
decorated_power = res2bin(power)

print(decorated_power(2, 3))
print(decorated_power(4, 5))

"""
Usando @ para decorar:
Python ofrece una sintaxis par simplificar la aplicación de los decoradores a través del operador @ justo antes de la definición de la función.
"""


@res2bin
def power(x: int, n: int) -> int:
    return x**n


print(power(5, 2))
print(power(10, 2))

"""
Manipulando argumentos:
"""


def assert_int(func):
    def wrapper(value1: int, value2: int, /) -> int | float | None:
        if isinstance(value1, int) and isinstance(value2, int):
            return func(value1, value2)
        return None

    return wrapper


# Aplicando el decorador
@assert_int
def add(a, b):
    return a + b


print(add(3, 4))
# print(add(5, 'a')) # error ✖️
# print(add('a', 'b')) # error ✖️

"""
Multiples decoradores: 
Permite aplicar más de un decorador a cada función.
"""


def plus5(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 5

    return wrapper


def div2(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result // 2

    return wrapper


@plus5
@div2
def prod(a, b):
    return a * b


result_prod = prod(4, 3)

print(result_prod)
print(((4 * 3) // 2) + 5)

"""
Funciones recursivas:
La recursividad es el mecanismo por el cual una función se llama a sí misma.
"""


def call_me():
    return call_me()


def pow(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    # Recursividad
    return base * pow(base, exponent - 1)


print(pow(2, 4))
print(pow(3, 5))

"""
Funcionitis: Es una inflamación en la zonal funcional, por querer aplicar funciones donde no es necesario.
"""


def inList(item: int, items: list[int]) -> bool:
    return item in items


print(inList(1, [1, 2, 3]))

print(1 in [1, 2, 3])  # That easy!

"""
Espacios de nombres:
Los espacios de nombres permite definir ámbitos o contextos en los que agrupar nombres de objetos. Proporcionan un mecanismo de empaquetado.
"""

# Acceso a variables globales: Acceder desde cualquier parte
language = "castellano"


def catalonia():
    print(f"{language=}")


print(language)

catalonia()

# Creando variables locales
language2 = "ingles"


def english():
    language2 = "catalan"
    print(f"{language2=}")


print(language2)
english()
print(language2)

"""
Forzando modificación global: Python permite modificar una variable definida en un espacio de nombres global dentro de una función. Para ello debemos usar el modificador 'global'. ✖️ NO SE CONSIDERA UNA BUENA PRÁCTICA

globals(): Devuelve un diccionario con los contenidos del espacio de nombres global.
"""

language = "castellano"


def catalonia():
    global language
    language = "catalan"
    print(f"{language=}")


print(language)

catalonia()

print(language)

# Contenido de los espacios de nombres
language = "english"


def catalonia2():
    language = "catalan"
    print(f"{locals()=}")


catalonia2()
