"""
La sentencia While (Mientras):
Permite repetir instrucciones mientras se cumpla una condición.
"""

""" want_greet = "S"

while want_greet == "S":
    print("Hola")
    # Preguntar por teclado si desea repetir
    want_greet = input("¿Quieres saludar otra vez? (S/N)")

print("Adios!") """

"""
Romper un bucle while:
Con la palabra reservada 'break' se puede romper un bucle mientras.
"""

""" MAX_GREETS = 4
nums_greet = 0
want_greet = "S"

while want_greet == "S":
    print("Hola")
    nums_greet += 1
    if nums_greet == MAX_GREETS:
        print("Máximo de saludos alcanzado")
        break # Rompe el bucle
    want_greet = input("¿Quieres saludar otra vez? (S/N)")

print("Adios!") """

"""
Continuar un bucle while:
Con la palabra reservada 'continue' se puede continuar con el siguiente
"""

""" want_greet = "S"

valid_options = 0

while want_greet == "S":
    print("Hola")
    want_greet = input("¿Quieres saludar otra vez? (S/N)")
    if want_greet not in "SN":
        print("No le he entendido pero le voy a saludar otra vez")
        want_greet = "S"
        continue  # Continua con el bucle
    valid_options += 1
print(f"{valid_options} saludos válidos")

print("Adios!") """

"""
Bucle infinito: 
Si no se establece la condición de parada o bien el valor de alguna variable está fuera de control, es mejor reescribir la condición de parada.
"""

""" num = 1

while num < 10:
    print(num)
    num += 2  # Incrementa el valor de num, no entra en un bucle infinito

while 0 <= (mark := float(input("Introduce una nueva nota: "))) <= 100:
    print("NOTA:", mark)
print("Nota fuera de rango! ❌")
"""

"""
Sentencia FOR.
Permite recorrer aquellos tipos de datos que sean iterables (listas, tuplas, diccionarios, etc.)
"""

word = "Python"

for letter in word:
    print(letter)
"""
Romper un bucle for:
Con la palabra reservada 'break' se puede romper un bucle for.
"""

word2 = "JavaScript"

for letter in word2:
    if letter == "v":
        break  # Rompe el bucle
    print(letter)

"""
Secuencia de Números:
start: Es opcional y tiene por defecto el valor 0.
stop: Es obligatorio. Siempre se llega a 1 menos que este valor.
step: Es opcional y tiene por defecto el valor 1.
"""

for i in range(0, 3):
    print(i)

for i in range(3):  # No hace falta indicar el inicio
    print(i)

for i in range(1, 6, 2):
    print(i)

for i in range(2, -1, -1):
    print(i)

"""
Usando el guión bajo:
Es el nombre de la variable que se va a iterar.
"""

for _ in range(11):
    print("Repetir 11 veces")

"""
Usando el guión bajo y el guión alto:
Es el nombre de la variable que se va a iterar.
"""

for _ in range(11):
    print("Repetir 11 veces")

"""
Bucles for anidados:
"""

for num_table in range(1, 10):
    for mul_factor in range(1, 10):
        result = num_table * mul_factor
        print(f"{num_table} * {mul_factor} = {result}")
