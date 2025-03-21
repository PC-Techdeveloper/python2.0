"""
Tipos de datos
Booleano -> bool -> True, False
Entero -> int -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Flotante -> float -> 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0
Complejo -> complex -> 1j, 2j, 3j, 4j, 5j, 6j, 7j, 8j, 9j, 10j
Cadena -> str -> "Hello World"
Lista -> list -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Conjunto -> set -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Diccionario -> dict -> {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
"""

"""
Variables:
Las variables son fundamentales ya que permiten definir nombres para los valores que tenemos en memoria.
"""

"""
Asignacion:
"""
# Asignación de variables.
total_population = 157_503

avg_temperature = 16.8

city_name = "Buenos Aires"

# Asignación de constantes
SOUND_SPEED = 343.2
WATER_DENSITY = 1000
EARTH_NAME = "Earth"

# Python ofrece una asignación múltiple.
tres = three = dre1 = 3

# Python ofrece tipar variables (opcional).
name: str = "John"

print(name)

"""
Asignando una variable a otra variable.
"""

people = 1232

total_population = people

print(total_population)

# Conocer el valor de una variable.
final_stock = 2543
print(final_stock)

"""
Conocer el tipo de una variable:
Para poder descubrir el tipo de un literal o una variable.Python ofrece la función type().
"""

print(type(9))
print(type(1.3))

height = 234
print(type(height))

SOUND_SPEED = 56.76
print(type(SOUND_SPEED))

"""
Mutabilidad:
Las variables pueden cambiar su valor, pero no pueden cambiar su tipo.

Tipos de objetos según su naturaleza de cambio:
inmutable: bool, int, float, str, tuple.
mutable: list, set, dict.
"""

