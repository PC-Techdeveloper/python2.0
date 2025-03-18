"""
Un conjunto representa una serie de valores únicos y sin orden establecido.
"""

# Creando conjuntos

lottery = {21, 10, 46, 29, 31, 94}

print(lottery)

# Conjunto vacío

wrong_empty_set = {}

print(type(wrong_empty_set))  # Devuelve un dict.

# Creando un conjunto vacío correctamente

empty_set = set()

print(type(empty_set))  # Devuelve un set.

"""
Conversión:
"""
# set()
print(set("aplatanada"))
print(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]))
print(set(("ADENINA", "TIMINA", "TIMINA", "GUANINA", "ADENINA", "CITOSINA")))
print(set({"manzana": "rojo", "plátano": "amarillo", "kiwi": "verde"}))

"""
Obtener un elemento:
En un conjunto no existe un orden establecido para sus elementos, por lo tanto no se puede acceder a un elemento en particular., al igual que no se puede modificar un elemento existente.
"""

# Añadir un elemento

beatles = set(["Lennon", "McCartney", "Harrison", "Starr"])

beatles.add("Best")

print(beatles)

periodic_table = set()
metails = ("Fe", "Mg", "Au", "Au", "Zn")

periodic_table.add(metails)

non_metals = ("H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne")
periodic_table.add(non_metals)

print(periodic_table)

"""
Borrar elementos:
"""
# Función remove()

beatles.remove("Lennon")

print(beatles)

"""
Longitud de un conjunto:
"""

# Función len()

print(f"Longitud:", len(beatles))

"""
Iterar sobre un conjunto:
"""

# La forma de recorrer los elementos de un conjunto es utilizando la sentencia for

for beatle in beatles:
    print(beatle)

"""
Pertenencia de un elemento:
"""

# Operador in
print("Harrison" in beatles)
print("Farina" in beatles)
print("Ryan" in beatles)
print("Lennon" not in beatles)

"""
Ordenando un conjunto: Los conjuntos no mantienen un orden, pero que ocurrirá si son ordenados.
"""

marks = {8, 4, 5, 2, 9, 5}

print(sorted(marks))  # Devuelve una lista con los elementos ordenados

# print(marks.sort()) # error: ✖️

"""
Teoria de conjuntos:
* Intersección: Elementos que están en a la vez en A y en B.
* Unión: Elementos que están tanto en A como en B.
* Diferencia: Elementos que están en A pero no en B.
* Diferencia simétrica: Elementos que están en A o en B pero no en ambos conjuntos.
"""
print("------ Teoria De Conjuntos ------")
# Intersección
a = {1, 2}
b = {2, 3}

print(f"Intersección:", a.intersection(b))
print(a & b)

# Unión
print(f"Unión:", a.union(b))
print(a | b)

# Diferencia
print(f"Diferencia:", a.difference(b))
print(a - b)

# Diferencia simétrica
print(f"Diferencia simétrica:", a.symmetric_difference(b))
print(a ^ b)

print("------ Inclusión ------")

"""
* Un conjunto B es un subconjunto de otro conjunto A si todos los elementos de B están incluidos en A.
* Un conjunto A es un superconjunto de otro conjunto B, si todos los elementos de B están incluidos en A.
"""

A = {2, 4, 6, 8, 10}
B = {4, 6, 8}

# Subconjunto
print(f"Subconjunto:", B.issubset(A))
print(B < A)
print(B <= A)

# Superconjunto
print(f"Superconjunto:", A.issuperset(B))
print(A > B)
print(A >= B)

a = {3, 5, 7, 9}
b = {1, 3, 5}

print(b < a)  # 1 no está en a, devuelve False

"""
Conjuntos por comprensión:
"""
m3 = {number for number in range(0, 20) if number % 3 == 0}
print(m3)

"""
Conjuntos inmutables:
Crear conjuntos inmutables haciendo uso de la función frozenset(), que recibe cualquier iterable como argumento.
"""

marks = {1, 3, 2, 3, 1, 4, 2, 4, 5, 2, 5, 5, 3, 1, 4}

marks_levels = frozenset(marks)

print(marks_levels)

# marks_levels.add(50)  # error: no se puede modificar ✖️

CHESE_PIECES = frozenset(("king", "queen", "rook", "bishop", "knight", "pawn"))

print(CHESE_PIECES)
