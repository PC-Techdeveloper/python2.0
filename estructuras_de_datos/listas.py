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
Número de ocurrencias: Para contar cuantas veces aparece un determinado valor dentro de una lista podemos usar la función count():
"""

sheldon_greeting = ["Penny", "Penny", "Penny"]

print(sheldon_greeting.count("Penny"))

print(sheldon_greeting.count("Howard"))

"""
Sividir una cadena de texto en lista: Dividirla por un separador con la función split(), devuelve una lista donde cada elemento es una parte de la cadena del texto original.
"""

proverb = "No hay mal que por bien no venga"

proverb_list = proverb.split()

print(proverb_list)

tools = "Martillo,Sierra,Destornillador"

tools_list = tools.split(",")

print(tools_list)

game = "piedra-papel-tijera"

print(type(game_tools := game.split("-")))

print(game_tools)

"""
Particionado de cadenas de texto: Python ofrece la función partition(), el resultado es una tupla; para dividir una cadena de texto en dos partes, una con un determinado carácter y otra con el resto de la cadena.
"""

text = "3 + 4"

print(text.partition("+"))

"""
Unir una lista en cadena de texto: Añade un separador entre cada elemento de la lista y devuelve una cadena de texto.
"""

shopping = ["Agua", "Huevos", "Aceite"]

shopping_string = "--".join(shopping)

print(shopping_string)

"""
Ordenar una lista: 
"""

## Conservando la lista original

languages = ["Python", "Ruby", "JavaScript", "Java", "C++"]

## sorted(): Devuelve una nueva lista ordenada
print(sorted(languages))

## Modificando la lista original

## sort():

languages = ["Python", "Ruby", "JavaScript", "Java", "C++"]

languages.sort()

print(languages)

## reverse, para indicar el orden inverso de la lista

languages = ["Python", "Ruby", "JavaScript", "Java", "C++"]

print(sorted(languages, reverse=True))

"""
ITERAR SOBRE UNA LISTA: Podemos iterar sobre elementos de una lista usando la sentencia for:
"""

shopping3 = ["Agua", "Huevos", "Aceite", "Sal", "Limon"]

for item in shopping3:
    print(item)

## Iterar usando enumeración para saber el indice del elemento

for i, item in enumerate(shopping3):
    print(f"Indice {i}: {item}")

## Iterar sobre multiples listas
"""
Python ofrece la posibilidad de iterar sobre multiples listas en paralelo utilizando la función zip(). Se basa en ir juntando ambas listas elemento a elemento
"""

shopping = ["Agua", "Aceite", "Arroz"]

details = ["mineral natural", "fresco", "salado"]

for product, detail in zip(shopping, details):
    print(product, detail)

## Obtener una lista explicita con la combinación en paralelo de las listas
shoes = ["Nike", "Reebok", "Asics"]

details_shoes = ["rojo", "azul", "amarillo"]

print(list(zip(shoes, details_shoes)))

"""
Comparar listas:
"""

print([1, 2, 3] < [1, 2, 4])

"""
CUIDADO CON LAS COPIAS: Las listas son estructuras de datos mutables y esta caracteristica obliga a tener cuidado cuando realizamos copias, ya que la modificación de una de ellas puede afectar a la otra.
"""

original_list = [4, 3, 7, 1]

## Copy(): No modifica la lista original
copy_list = original_list.copy()

original_list[0] = 15

print(original_list)

print(copy_list)

copy_list = original_list[:]

print(id(original_list) != id(copy_list))

"""
Veracidad multiple: para comprobar la veracidad de determinadas expresiones, Python nos ofrece dos funciones «built-in» con las que podemos evaluar si se cumplen todas las condiciones all() o si se cumple alguna condición any(). Estas funciones trabajan sobre iterables, y el caso más evidente es una lista.
"""

word = "python"

enough_length = len(word) > 4
right_beginning = word.startswith("p")
min_ys = word.count("y") >= 1
## Versión con veracidad múltiple usando all()
is_cool_word = all([enough_length, right_beginning, min_ys])

if is_cool_word:
    print("¡Is a good word ✅!")
else:
    print("¡No thanks ✖️!")

word = "yeah"

enough_length = len(word) > 4
right_beginning = word.startswith("p")
min_ys = word.count("y") >= 1

## Versión con veracidad múltiple usando any()
is_fine_word = any([enough_length, right_beginning, min_ys])

if is_fine_word:
    print("¡Is a Fine word ✅!")
else:
    print("¡No thanks ✖️!")

## Tener en cuenta la peculiaridad cuando se trabajan con listas vacias
print(all([]))

print(any([]))

"""
Listas por comprensión: Establecen una técnica para crear listas de forma más compacta basándose en el concepto matemático de conjuntos definidos por compresión.
"""
values = "32,45,11,87,20,48"
int_values = [int(value) for value in values.split(",")]
print(int_values)

## Condiciones en comprensiones
values = "32,45,11,87,20,48"
int_values = [int(v) for v in values.split(",") if v.startswith("4")]
print(int_values)

"""
sys.argv: Ejecutar programa desde la línea de comandos, acceder a los argumentos de dicho programa. Para ello se utiliza una lista especial que se encuentra dentro del  módulo sys y se denomina argv.
"""

"""
Funciones matemáticas:
"""

## Suma de todos los valores
data = [5, 3, 2, 8, 9, 1]
print(sum(data))

## Mínimo de todos los valores
data = [5, 3, 2, 8, 9, 1]
print(min(data))

## Máximo de todos los valores
data = [5, 3, 2, 8, 9, 1]
print(max(data))

"""
Listas de listas
"""
goalkeeper = "cata"
defenders = ["olga", "laia", "trene", "ona"]
midfielders = ["jenni", "teresa", "aitana"]
forwards = ["mariona", "salma", "alba"]

team = [goalkeeper, defenders, midfielders, forwards]
print(team)

# Comprobar el acceso a distintos elementos
print(team[0])
print(team[2])
print(team[3][1])

# Recorrer la lista
for playline in team:
    if isinstance(playline, list):
        for player in playline:
            print(player, end=" ")
        print()
    else:
        print(playline)

from collections import deque

deque()

print(deque(["a", "b", "c", "d"]))

llist = deque("abcdefghij")
llist.appendleft("z")
print(llist.popleft())
print(llist)
