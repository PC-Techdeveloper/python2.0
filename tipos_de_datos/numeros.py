"""
Booleanos: Son valores que pueden ser True o False.
"""

is_opened = True

print(is_opened)

has_sugar = False

print(has_sugar)

"""
Enteros: Los números enteros no tienen decimales pero si pueden contener signo y estar expresando alguna base distinta de la usual (base 10)
"""

# Literales enteros

print("--- Literales Enteros ---")
print(8)
print(0)
print(99)
print(+99)
print(1000000)
print(-1000000)
print(3_000_000)

"""
Operaciones con enteros:

+ -> suma
- - > resta
* -> multiplicacion
/ -> división
//  -> división entera
%  -> modulo
** -> potencia
>> -> bits a la derecha
<< -> bits a la izquierda

PRIORIDAD DE LOS DISTINTOS OPERADORES:

1. (mayor) ()
2. **
3. -a +a
4. * / // %
5. (menor) + -
"""

print("--- Operaciones con enteros ---")

print(2 + 8 + 4)
print(4**4)
print(7 / 3)
print(7 // 3)
# print(6 / 0) # Error ❌
print(6 % 3)

print("--- Prioridad de los distintos operadores ---")

print(2**2 + 4 / 2)
print(2 ** (2 + 4) / 2)
print(2 ** (2 + 4 / 2))

"""
Asignación aumentada: += -= *= /= //= %=
"""

total_cars = 100

sold_cars = 20

total_cars -= sold_cars

print(total_cars)

random_number = 15

random_number += 5
print(random_number)

random_number *= 3
print(random_number)

random_number //= 4
print(random_number)

random_number **= 1
print(random_number)

"""
Módulo: Es el resto de la división de dos números.
"""

dividendo = 17

divisor = 5

cociente = dividendo // divisor

resto = dividendo % divisor

print(cociente)
print(resto)

"""
Cuando el dividendo es múltiplo del divisor, su módulo es cero.
"""

print(12 % 3)
print(15 % 5)
print(21 % 7)
print(81 % 9)

"""
Exponenciación: Es la potencia de un número.
"""

print(4**3)
print(4 * 4 * 4)
print(4**0.5)

"""
Valor absoluto: Es el valor absoluto de un número. Python ofrece la función abs().
"""

print(abs(-5))
print(abs(5))
print(abs(0))
print(abs(-3.14))
print(abs(3.14))

## Limite de un número

centillion = 10**600
print(centillion)

"""
Flotantes:
Los números flotantes tienen parte decimal.
"""

print("--- Flotantes ---")

print(4.0)
print(04.0)
print(4.000_000)

"""
Conversión de tipos:

Conversión implicita:

bool-int -> int
bool-float -> float
int-float -> float
True -> 1
False -> 0

Conversión explícita:
bool(), int(), float()
"""

## Conversión implicita: Python convierte automáticamente un número a otro tipo.
print("--- Conversión implicita ---")

print(True + 25)
print(7 * False)
print(True + False)
print(21.8 + True)
print(10 + 11.3)

print("--- Conversión explícita ---")

print(bool(1))
print(bool(0))
print(int(True))
print(int(False))
print(float(1))
print(float(0))
print(float(True))
print(float(False))

# int() sobre un número flotante retorna el entero más cercano.

print("--- int() sobre un número flotante retorna el entero más cercano ---")

print(int(3.1))
print(int(3.5))
print(int(3.9))

## Obtener el tipo de variable

is_raining = False

print(type(is_raining))

SOUND_LEVEL = 35

print(type(SOUND_LEVEL))

temp = 36.6

print(type(temp))

## También comprobar el tipo mediante la función isinstance()

print(isinstance(is_raining, bool))
print(isinstance(SOUND_LEVEL, int))
print(isinstance(temp, float))

"""
Bases:
Los valores numéricos con los que estamos acostumbrados a trabajar están en base 10 (o decimal). Esto indica que disponemos de 10 «símbolos» para representar las cantidades. En este caso del 0 al 9.

Pero también es posible representar números en otras bases. Python nos ofrece una serie de prefijos y funciones para este cometido.
"""

"""
Base binaria: Cuenta con 2 símbolos: 0 y 1.
"""

print("--- Base Binaria ---")

# Prefijo: 0b
print(0b1001)
print(0b1100)

# Función: bin() - Devuelve un string con los números binarios.
print(bin(9))
print(bin(12))

print("--- Base Octal ---")

# Prefijo: 0o: Cuenta 8 símbolos: 0, 1, 2, 3, 4, 5, 6, 7
print(0o6243)
print(0o1257)

# Función: oct() - Devuelve un string con los números octales.
print(oct(3225))
print(oct(687))

print("--- Base Hexadecimal ---")

# Prefijo: 0x: Cuenta con 16 símbolos: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
print(0x7F2A)
print(0x48FF)

# Función: hex() - Devuelve un string con los números hexadecimales.
print(hex(32554))
print(hex(18687))
