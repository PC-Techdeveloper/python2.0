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

# Obtener un elemento
print(rae["anarcoide"])
# print(rae["access"]) # ✖️ error: no existe

"""
Usando get(): 
Si la clave que buscamos EXISTE, devuelve su valor.
Si la que buscamos NO EXISTE, devuelve None (Salvo que se le indique otro valor por defecto, pero en ninguno de los dos casos obtendrá un error).
"""

print(rae.get("bifronte"))
print(rae.get("programacion", "No disponible"))

"""
Añadir o modificar elementos:
Para añadir elementos a un diccionario sólo es necesario hacer referencia a la CLAVE y asignarle un VALOR:

Si la clave YA EXISTE, se reemplaza el valor existente por el nuevo valor.
Si la clave NO EXISTE, se añade la clave y el valor.
"""

# Añadir un nuevo elemento
rae["enjuiciar"] = "Someter una cuestión a examen, discusión y juicio"

print(rae)

# Modificar un elemento existente
rae["enjuiciar"] = "Instruir, juzgar o sentenciar una causa"

print(rae)

"""
Crear diccionario desde vacío:
"""

VOWELS = "aeiou"

enum_vowels = {}

for i, vowel in enumerate(VOWELS, start=1):
    enum_vowels[vowel] = i

print(enum_vowels)

"""
Pertenencia de una clave:
"""
print("bifronte" in rae)
print("almohada" in rae)
print("montuvio" in rae)

"""
Longitud de un diccionario: 🟡
"""
