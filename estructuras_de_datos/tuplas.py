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

## Función tuple()

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
