"""
Las listas permiten almacenar objetos mediante un orden definido y con posibilidad de duplicados. Las listas son estructuras de datos mutables, lo que significa que podemos añadir, eliminar y modificar elementos dentro de ellas.
"""

# Creando listas: Una lista esta compuesta por zeros o más elementos

empty_list = []

languages = ["Python", "Ruby", "JavaScript"]

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]

data = ["Tenerife", {"cielo": "limpio", "temp": 24}, 3718, (28.29333947, -16, 5226597)]

# Conversión: funcion list()

# conversión desde una cadena de texto
print(list("Python"))

print(list(range(10)))  # lista explicita

# lista vacia
print(list())

"""
Operaciones con listas
"""

## Obtener un elemento: Obtener a través del índice

shopping = ["Agua", "Huevos", "Aceite"]

print(shopping[0])
print(shopping[1])
print(shopping[2])
print(shopping[-1])  # Acceso con índice negativo
# print(shopping[3])  # error: No existe en la lista ✖️

## Trocear una lista: Extraer elementos de una lista

shopping = ["Agua", "Huevos", "Aceite", "Sal", "Limon"]

print(shopping[0:3])
print(shopping[:3])
print(shopping[2:4])
print(shopping[-1:-4:-1])
# Equivale a invertir una lista
print(shopping[::-1])

# Python restringirá a los limites de la lista
print(shopping[10:])
print(shopping[-100:2])
print(shopping[2:100])

"""
Invertir una lista: Cambiar el orden de los elementos
"""

## Conservando la lista original
print(shopping[::-1])

# Función reversed()
print(list(reversed(shopping)))

## Modificando la lista original

languages = ["Python", "Ruby", "JavaScript", "Java", "C++"]

languages.reverse()

print(languages)

## Añadir al final de la lista
brands = ["Nike", "Adidas", "Puma", "Reebok", "Asics"]

brands.append("New Balance")

print(brands)

## Creando desde vacío
even_numbers = []
# Iterando sobre un range
for i in range(11):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

## Añadir en cualquier posición de una lista

even_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers.insert(0, "Jamon")

print(even_numbers)

## Repetir elementos

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

repeat_numbers = numbers * 2

print(repeat_numbers)

"""
Combinar listas: Unir dos listas en una nueva lista

Función extend(): Recorre o itera sobre cada uno de los elementos del objeto
Función append(): Añadira como una sublista de la lista principal
"""

shopping = ["Agua", "Huevos", "Aceite"]

fruitshop = ["Frutas", "Verduras", "Manzanas"]

## Conservando la lista original
combined = shopping + fruitshop

print(combined)

## Modificando la lista original

# extend()
shopping.extend(fruitshop)

print(shopping)

# Append()
shopping.append(fruitshop)

print(shopping)

## Modificar una lista

shopping[0] = "Frutas"
# shopping[100] = "Jugo"  # error: No existe en la lista ✖️
print(shopping)

## Modificar con troceado

fruitshop = ["Frutas", "Verduras", "Manzanas", "Sal", "Limon"]

fruitshop[1:4] = ["Nuggest", "Atún"]

print(fruitshop)

## Borrar elementos: Python ofrece cuatro formas para borrar elementos en una lista

shopping2 = ["Agua", "Huevos", "Aceite", "Sal", "Limon", "Limon"]

# Por su índice: del
del shopping2[3]

print(shopping2)

# Por su valor: remove() | Si existen duplicados, solo borrará la primera ocurrencia
shopping2.remove("Limon")

print(shopping2)

# Por su índice: pop() | Borra y devuelve el elemento

product = shopping2.pop(2)

product_eggs = shopping2.pop(1)

# empty_product = shopping2.pop() # devuelve -1 el ultimo elemento

print(product)

print(product_eggs)

# Por su rango: Mediante troceado de listas

products = ["Laptop", "Phone", "Eggs", "Juice", "Tablet", "Fruits"]

products[1:4] = []

print(products)

"""
Borrado completo: Python ofrece al menos dos formas para borrar una lista por completo.
"""

foods = ["Frutas", "Verduras", "Manzanas", "Azucar", "Limon", "Mango"]

## Clear()
foods.clear()

print(foods)

## Reinicializar la lista a vacía con []

foods = []

print(foods)

"""
Encontrar un elemento: 
"""

## Descubrir el índice de un elemento

third_shopping = ["Agua", "Huevos", "Aceite", "Sal", "Limon"]

print(third_shopping.index("Huevos"))
# print(third_shopping.index("Aguacate")) # ✖️ error: no existe


"""
Pertenencia de un elemento: Comprueba la existencia de un determinado elemento en una lista

El operador IN siempre devuelve un valor booleano (True o False)
"""

shopping = ["Agua", "Huevos", "Aceite", "Sal", "Limon"]

print("Agua" in shopping)  # True ✅
print("Pollo" in shopping)  # False ✖️

"""
Número de ocurrencias: 🟡
"""
