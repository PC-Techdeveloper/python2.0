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
Longitud de un diccionario: 
"""
print(len(rae))

"""
Obtener todos los elementos:
"""

# Todas las claves de un diccionario
print(rae.keys())

# Todos los valores de un diccionario
print(rae.values())

# Todos los pares clave-valor de un diccionario
print(rae.items())

"""
Iterar sobre un diccionario:
"""

# Iterar sobre las claves
for word in rae.keys():
    print(word)

# Iterar sobre los valores
for meaning in rae.values():
    print(meaning)

# Iterar sobre los pares clave-valor
for word, meaning in rae.items():
    print(word, meaning)

"""
Borrar elementos:
"""

# Mediante su clave: del
del rae["bifronte"]

print(rae)

# Por su clave (con extracción)
rae.pop("anarcoide")

print(rae)
# print(rae["bucle"])  # ✖️ error: no existe

# Borrado completo del diccionario
rae.clear()

print(rae)  # Borra el contenido de la variable

# Reinicialzando el diccionario a vacío con {}
# Creando una nueva variable vacía
rae = {}
print(rae)

"""
Combinar diccionarios:

Si la clave no existe, se añade con su valor.
Si la clave ya existe, se añade con el valor del último diccionario en la mezcla.
"""

rae1 = {
    "bifronte": "De dos frentes o dos caras",
    "enjuiciar": "Someter una cuestión a examen, discusión y juicio",
}

rae2 = {
    "anarcoide": "Que tiende al desorden",
    "montuvio": "Campesino de la costa",
    "enjuiciar": "Instruir, juzgar o sentenciar una causa",
}

# Sin modificar los diccionarios originales
# Mediante el operadoar **

print({**rae1, **rae2})

# Mediante el operador |

print(rae1 | rae2)

# Modificando los diccionarios originales
# Mediante la función update()

rae1.update(rae2)

print(rae1)

"""
Copias de diccionarios:
"""

# Mediante la función copy()
original_rae = {
    "name": "guido",
    "surname": "van rossum",
    "job": "python creator",
}

copy_rae = original_rae.copy()

original_rae["name"] = "Jefferson"

print(original_rae)

print(copy_rae)

## En caso de que se este trabajando con elementos mutables, se hace uso
## de la función deepcopy() dentro del módulo copy de la librería estándar

import copy

original_dict = {
    "name": "Juan",
    "age": 30,
    "hobbies": ["read", "write", "code"],
    "address": {"city": "Madrid", "country": "Spain"},
}

copy_shallow = copy.copy(original_dict)

copy_deep = copy.deepcopy(original_dict)

original_dict["hobbies"].append("sport")
original_dict["address"]["city"] = "Barcelona"

original_dict["address"]["country"] = "France"

print(f"address: {original_dict}")
print(f"copy_shallow: {copy_shallow}")
print(f"copy_deep: {copy_deep}")

"""
Diccionarios por comprensión:
Podemos aplicar este método usando llaves ({ })
"""

words = ("sun", "space", "rocket", "earth")
words_length = {word: len(word) for word in words}
print(words_length)

# Aplicar condiciones a estas comprensiones
words = ("sun", "space", "rocket", "earth")
words_length = {w: len(w) for w in words if w[0] not in "aeiou"}
print(words_length)

"""
Objetos hashables: Un objeto, es hashable si se le pueede asignar un valor hash que no cambia en ejecución durante toda su vida. Para encontrar el has de un objto se puede utilizar la función hash(), que devuelve un número entero y es utilizado para indexar la tabla hash que se mantiene internamente en la memoria de la computadora.
"""

print(hash(999))
print(hash(3.14))
print(hash("hello"))
print(hash(("a,", "b", "c")))
# Para que un objeto sea hashable, debe ser inmutable
print(hash([1, 2, 3]))
