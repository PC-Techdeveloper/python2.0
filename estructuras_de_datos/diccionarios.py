"""
Un diccionario es un objeto indexado por claves que tienen asociados los valores. Mantienen el orden en el que se insertan las claves, son mutables, las claves deben ser únicas, tienen un acceso muy rápido a sus elementos.
"""

# Creando diccionarios

empty_dict = {}

rae = {
    "bifronte": "de dos frentes o dos caras",
    "anarcoide": "que tiende el desorden",
    "montuvio": "campesino de la costa",
}

population_can = {
    2015: 2_135_209,
    2016: 2_154_924,
    2017: 2_177_048,
    2018: 2_206_901,
    2019: 2_220_270,
}

print(rae)
print(population_can)

"""
Conversión:
"""

# dict()

## Diccionario a partir de una lista de cadenas de texto
print(dict(["a1", "b2"]))

## Diccionario a partir de una tupla de cadenas de texto
print(dict(("a1", "b2")))

## Diccionario a partir de una lista de listas
print(dict([["a", 1], ["b", 2]]))

# Diccionario vacío sin argumentos
print(dict())
print(dict({}))

"""
Crear diccionario con dict(): 
También es posible utilizar la función dict() para crear diccionarios y no tener que utilizar llaves y comillas.
"""

person = dict(name="guido", surname="van rossum", job="python creator")

print(person)

# Crear un diccionario eespecificando sus claves y un único valor de relleno.
my_dictionary = dict.fromkeys("aeiou", 1)
print(my_dictionary)

"""
Operaciones con diccionarios:

"""
