"""
Comentarios:
Los comentarios son anotaciones que permiten incluir en el programa y aclarar aspectos del código.
"""

# Universe age expressed in days
universe_age = 13800 * (10**6) * 365
stock = 0  # Release additional articles

"""
Sentencia IF-ELSE:
Añadir una expresión de comparación terminando con dos puntos al final de la línea. En caso de que no se cumpla se usa la sentencia ELSE.
"""

temp = 20

if temp > 35:
    print("Aviso por temperatura alta ⚠️")
else:
    print("Temperatura normal ☀️")

# Condiciones anidadas
temp = 28

if temp < 20:
    if temp < 10:
        print("Nivel azul 🟦")
    else:
        print("Nivel verde 🟩")
elif temp < 30:
    print("Nivel naranja 🟧")
else:
    print("Nivel rojo 🟥")

"""
Asignaciones condicionales:
"""

temp = 35

if temp < 30:
    fire_risk = "LOW"
else:
    fire_risk = "HIGH"

print(fire_risk)

# Abreviación de la sentencia IF-ELSE
fire_risk = "LOW" if temp < 30 else "HIGH"
print(f"El riesgo de incendios es {fire_risk}")

"""
Operadores de comparación:
Igualdad

==
Desigualdad: !=

Menor que: <

Menor o igual que: <=

Mayor que :>

Mayor o igual que: >=
"""

print("---- Operadores de Comparación ----")
value = 8
print(value == 8)
print(value != 8)
print(value < 12)
print(value <= 7)
print(value > 4)
print(value >= 9)

# Python ofrece la posibilidad de ver si un valor está entre dos límites
# de manera directa:

x = 8

print(4 <= x <= 12)

"""
Operadores lógicos:
and , or , not
"""

print("---- Operadores Lógicos ----")

"""
Tabla de la verdad:

OR.

True or True: True
False or True: True
True or False: True
False or False: False

AND: 

True and True: True
True and False: False
False and True: False
False and False: False

NOT:

!True: False
!False: True
"""
x = 8

print(x > 4 or x > 12)
print(x < 4 or x > 12)
print(x > 4 and x > 12)
print(x > 4 and x < 12)
print(not (x != 8))

"""
Cortocircuito lógico: 
Las expresiones lógicas no se evalúan por completo si se dan una serie de circunstancias.
"""

# Ejemplo: Cortocircuito lógico or
print("--- Ejemplo: Cortocircuito lógico AND ---")
power = 10
signal_4g = 60
# Produce un cortocircuito sin evaluar el resto
print(power > 25 and signal_4g > 10)

print("--- Ejemplo: Cortocircuito lógico OR ---")

power = 50
signal_4g = 20
# Produce un cortocircuito sin evaluar el resto
print(power > 40 or signal_4g > 30)


"""
Booleanos en condicionales:
Consultar por la verocidad de una dterminada variable booleana en una condición
"""
is_cold = True

if is_cold:
    print("Ponte una chaqueta")
else:
    print("Ponte una camiseta")

is_cold = False

if not is_cold:
    print("Usa camiseta")
else:
    print("Usa chaqueta")

"""
Valor nulo:
None es un valor especial de Python que almacena el valor nulo. 
"""

val = None

if val:
    print(f"Value has some value: {val}")
else:
    # Value podría contener None, False (u otro valor)
    print("Value seems to be void")

value = 99

# el operador 'is' comprueba únicamente si los identificadores son el iguales
if value is not None:
    print(f"{value=}")

"""
Veracidad: 
La veracidad son los valores que evalúan a falso o evalúan a verdadero.
"""

print("--- Valores que evalúan a False ---")

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

print("--- Valores que evalúan a True")

print(bool("False"))
print(bool(" "))
print(bool(1e-10))
print(bool([0]))
print(bool("🦆"))

"""
Asignación Lógica: 
Es posible utilizar operadores lógicos en sentencias de asignación sacando partido de las tablas de la verdad.
"""
print("------------------")
b = 0
c = 5

a = b or c

print(a)

b = 0
c = 7

a = b and c

print(a)

"""
Sentencia match-case: 
Comparar valores: Permite comparar un valor de entrada con una serie de literales.
"""

color = "#00ff00"

match color:
    case "#ff0000":
        print("🟥")
    case "#00ff00":
        print("🟩")
    case "#0000ff":
        print("🟦")
    case _:
        print("Unknown color ❌")

"""
Patrones avanzados:
"""

point = (8, 3, 5)  # Notese el 8 como str

match point:
    case (int(x), int(y)):
        distToOrigin = {(x**2 + y**2) ** (1 / 2)}
    case (int(x), int(y), int(z)):
        distToOrigin = {(x**2 + y**2 + z**2) ** (1 / 2)}
    case _:
        print("Unknown point ❌")

print(distToOrigin)

"""
Operador morsa: 
Permite unificar sentencias de asignación dentro de expresiones. Su nombre proviene de la forma que adquiere :=
"""

radius = 4.25

if (perimeter := 2 * 3.14 * radius) < 100:
    print("Perimetro demasiado grande 🔥 ")
    print(f"Perimetro Actual: {perimeter}")
