# Una tupla es una secuencia de valores. Los valores pueden ser de cualquier
# tipo y están indexados por enteros, las tuplas son inmutables.
t = ('a', 'b', 'c', 'd', 'e')

# Crar una tupla con un solo elemento, se debe usar una coma al final.
t = 'a',
print(type(t))
# Un valor en paréntesis no es una tupla, es un string.
t2 = ('a')
print(type(t2))

# Otra manera de crear una tupla es usando la función tuple().
t = tuple()
print(t)

my_tuple = tuple('poppins')
print(my_tuple)

# La mayoría de las operaciones de las listas se pueden usar con las tuplas.
tuple1 = ('a', 'b', 'c', 'd', 'e')
print(tuple1[1])

# Slicing
print(tuple1[1:3])

# Como las tuplas son inmutables, no se pueden modificar.
# tuple1[1:3] = 'A'
# print(tuple1) # ❌ Error

# Se puede empezar una tupla con otra
tuple2 = ('A',) + tuple1
print(tuple2)

# Los operadores relacionales funcionan con las tuplas y otras secuencias
print((1, 2, 3) > (7, 8, 9))

"""
ASIGNACIÓN DE TUPLAS:
"""
path = 'monty@python.org'
# split(): Extrae una parte de una cadena
username, domain = path.split('@')
print(username)
print(domain)

"""
TUPLAS COMO VALORES DE RETORNO:
"""
# divmod() devuelve una tupla de dos valores, cociente y resto
tuple_div = divmod(7, 3)
print(tuple_div)

# O usar asignación de tuplas para almacenar los elementos por separado
quotient, remainder = divmod(7, 3)
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")


def min_max(t):
    return min(t), max(t)


min_max(range(11))

# Tuplas de argumentos de longitud variable
"""
Las funciones pueden tomar cantidad variable de argumentos. Un nombre de parámetro que comienza con * hace una reunión de argumentos en una tupla.
"""


def printall(*args):
    print(args)


printall(2, 4, 6, 8, 10)
printall(1, 2.0, '3')

"""
El complemento de la reunión es la dispersión 
"""

t = (7, 3)
print(divmod(*t))

print(max(1, 2, 3))

# sum() no permite dispersar
# print(sum(1, 2, 3))

"""
LISTAS Y TUPLAS
"""

# zip() toma dos o más secuencias y las intercala
s = 'abc'
t = [0, 1, 2]
print(zip(s, t))
