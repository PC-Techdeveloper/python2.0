"""
Las tuplas no admiten cambios y por lo tanto, es inmutable.
"""

# Creando tuplas

empty_tuple = ()

tenerife_geoloc = (28.46824, -16.25462)

three_wise_men = ("melchor", "gaspar", "baltasar")

# Tupla de un solo elemento: añadir una coma al final

one_item_tuple = ("papa noel",)
print(type(one_item_tuple))

# Tuplas sin paréntesis/str (NO RECOMENDADO) ✖️
one_item_tuple2 = "papa noel"
three_wise_men = "melchor", "gaspar", "baltasar"
tenerife_geoloc = 28.46824, -16.25462

print(type(one_item_tuple2))

# Modificar una tupla ✖️
three_wise_men = ("melchor", "gaspar", "baltasar")
# three_wise_men[0] = "tom and jerry"
# print(three_wise_men)

# Conversión

# Función tuple()

"""Esta conversión es válida para aquellos tipos que sean iterables: str, list, dist, set, etc. """
shopping = ["agua", "aceite", "arroz"]

shopping_tuple = tuple(shopping)

print(shopping_tuple)

# Convertir números a tuplas ✖️
# print(tuple(5))

# Tupla vacía without arguments
print(tuple())

"""
Operaciones con tuplas:
reverse()
append()
extend()
remove()
clear()
sort()
"""

"""Desempaquetado de tuplas:
Permite asignar una tupla a variables independientes.
"""

three_wise_men = ("melchor", "gaspar", "baltasar")

king1, king2, king3 = three_wise_men

print(king1, king2, king3)

# divmod(): Devuelve el cociente y el resto de una división
quotient, remainder = divmod(10, 3)
print(quotient, remainder)

"""
Intercambio de valores:
A través del desempaquetado de tuplas, se puede intercambiar los valores de una tupla.
"""
value1 = 40
value2 = 20

value1, value2 = value2, value1

print(value1, value2)

"""
Desempaquetado extendido:
También permite extender e indicar ciertos grupos de elementos  mediante el operador (*)
"""
ranking = ("G", "A", "R", "Y", "W")

head, *body, tail = ranking

print(head)
print(tail)
print(body)

# Usando solo dos elementos
head, *body = ranking

print(body)

*body, tail = ranking

print(body)
print(tail)

"""
Desempaquetado genérico:
El desempaquetado de tuplas es extensible a cualquier tipo de dato que sea iterable.
"""

# Sobre cadenas de texto
oxygen = "O2"
first, last = oxygen
print(first, last)

text = "Hello, world!"

head, *body, tail = text

print(head, body, tail)

# Sobre listas

writer1, writer2, writer3 = ["virginia woolf", "jane austen", "mary shelley"]

print(writer1, writer2, writer3)

text = "Hello, world!"

word1, word2 = text.split()

print(word1, word2)


"""
Tuplas por comprensión:
Los tipos de datos mutables (listas, diccionarios y conjuntos) si permiten comprensiones pero no así los tipos de datos inmutables como cadenas de texto y tuplas. Sin embargo, una tupla por comprensión genera un generador.
"""

my_range = (number for number in range(1, 6))

print(my_range)

"""
TUPLAS VS LISTAS:

TUPLAS: Ocupan menos espacio en memoria, existe protección frente a cambios indeseados, se pueden usar como claves de diccionarios.
"""
