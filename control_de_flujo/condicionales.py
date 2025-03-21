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
