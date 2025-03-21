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
x = 8

print(x > 4 or x > 12)
