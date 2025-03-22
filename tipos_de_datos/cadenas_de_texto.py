"""
Las cadenas de texto son secuencias de caracteres. También se les conoce como string y nos permiten almacenar información textual de forma muy cómoda.
"""

# Creandi strings

print("Mi primera cadena en Python")
print('Los llamados "strings" son secuencias de caracteres')
print("Los llamados 'strings' son secuencias de caracteres")

# Comillas triples
poem = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles"""

print("")

"""
Conversión:
Podemos crear strings a partir de otros tipos de datos usando la función str().
"""

print(str(True))
print(str(10))
print(str(21.7))

# Convertir de string a un valor numérico
print(int("10"))
print(float("21.7"))

# int() admite la base en la que se encuentra el número
print(int("FF", 16))

"""
Secuecnia de espace:
Permite escapar el significado de algunos caracteres para conseguir otros resultados. Se escribe una barra invertida \ antes del carácter en cuestión.
Escape más conocido es el \n, que permite insertar un salto de línea.
"""

# Salto de línea
message = "Primera línea\nSegunda línea\nTercera línea"
print(message)

# Tabulador
message = "Valor = \t40"
print(message)

# Comillas simples
message = "Necesitamos 'escapar' el 'carácter' que queremos"
print(message)

# Barra invertida
message = "Capítulo \\ Sección \\ Párrafo"
print(message)

"""
Expresiones literales:
Python trata el texto en bruto. Es el llamado raw-data y se aplica anteponiendo una "r" al comienzo de la cadena.
"""

text = "abc\ndef"
print(text)

text = r"abc\ndef"
print(text)

text = "a\tb\tc"
print(text)

text = r"a\tb\tc"
print(text)

"""
Más sobre print():
Admite algunos parámetros adicionales que permiten formatear la salida de la cadena.
"""

msg1 = "¿Sabes por qué estoy acá?"
msg2 = "Porque me apasiona"

print(msg1, msg1, sep="|")  # sep: separador
print(msg2, end="!!")  # end: caracter de final texto

print("\n")

"""
Leer datos desde el teclado: 
Los programas se hacen para interacción con el usuario. Una de las formas de interacción es solicitar la entrada de datos por teclado. Python ofrece también nos ofrece la posibilidad de leer la información introducida por teclado. para ello usamos la función input().
"""

# name = input("Introduzca su nombre: ")
# print(type(name))

# age = int(input("Introduzca su edad: "))
# print(type(age))

"""
Repetir cadenas: Podemos repetir dos o más cadenas de texto utilizando el operador *.
"""

reaction = "Wow"

print(reaction * 4)

"""
Obtener un caraácter: Los strings están indexados y cada carácter tiene su propia posición. Para obtener un único carácter dentro de una cadena de texto es necesario usar el operador [] específicando su índice dentro de los corchetes.
"""

sentence = "Esto es una prueba"

print(sentence[0])

print(sentence[-1])

print(sentence[4])

print(sentence[-5])

"""
Trocear una cadena: Podemos cortar una cadena de texto en dos o más partes utilizando el operador [:].
"""

proverb = "Agua pasda no muevo molino"

print(proverb[:])

print(proverb[12:])

print(proverb[:11])

print(proverb[5:11])

print(proverb[5:11:2])

"""
Longitud de cadena: Para obtener la longitud de una cadena podemos hacer uso de len()
"""

proverb = "Lo cortés no quita lo valiente"

print(len(proverb))

"""
Pertenencia de un elemento: Si queremos saber que una determinada subcadena se encuentra en una cadena de texto se utiliza el operador in para ello. Se trata de una expresión que tiene como resultado un valor booleano verdadero o falso.
"""

proverb = "Más vale malo conocido que bueno por conocer"

print("malo" in proverb)
print("bueno" in proverb)
print("regular" in proverb)

print("laptop" not in proverb)

"""
Limpiar cadenas: La función strip() se utiliza para eliminar caracteres del principio y del final de un «string».
"""

serial_number = "\n\t   \n 48374983274832    \n\n\t   \t   \n"

serial_number_clean = serial_number.strip()

print(serial_number_clean)

"""
Realizar búsquedas:
"""

lyrics = """Quizás porque mi niñez
Sigue jugando en tu playa
Y escondido tras las cañas
Duerme mi primer amor
Llevo tu luz y tu olor
Por dondequiera que vaya"""

# Comprueba si un string empieza o termina por alguna subcadena
print(lyrics.startswith("Quizás"))
print(lyrics.endswith("Final"))

# Encontrar la primera ocurrencia
print(lyrics.find("amor"))
print(lyrics.index("amor"))

# Contabilizar el número de veces que aparece una subcadena
print(lyrics.count("mi"))
print(lyrics.count("tu"))
print(lyrics.count("él"))

"""
Reemplazar elementos: Podemos usar la función replace() para reemplazar una subcadena por otra.
"""

proverb = "Quien mal anda mal acaba"
print(
    proverb.replace("mal", "bien", 1)
)  # 1 es el número de veces que queremos reemplazar

"""
Mayúsculas y minúsculas: Para convertir una cadena de texto a mayúsculas o minúsculas se usa la función upper(), lower(), capitalize(), title(), swapcase().
"""

phrase = "quien a buen árbol se arrima Buena Sombra le cobija"
print(phrase.capitalize())
print(phrase.title())
print(phrase.upper())
print(phrase.lower())
print(phrase.swapcase())

"""
Identificando caracteres: 
"""

# Detectar si todos los caracteres son letras o números
print("R2D2".isalnum())
print("C3-PO".isalnum())

# Detectar si todos los caracteres son numeros
print("314".isnumeric())
print("3.14".isnumeric())

# Detectar si todos los caracteres son letras
print("abc".isalpha())
print("a-b-c".isalpha())

# Detectar mayúsculas y minúsculas
print("BIG".isupper())
print("small".islower())
print("First Heading".istitle())

"""
Interpolación de cadenas:
Hace referencia al hecho de sustituir los nombres de variables por sus valores cuando se construye una cadena de texto.

Python ofrece tres formas de realizar esta tarea:

1. Antiguo: % 
2. Estilo nuevo: .format()
3. Estilo mdderno: f-strings: f''
"""

# f-strings
name = "Elon Musk"
age = 42
fortune = 43_300

print(f"Me llamo {name}, tengo {age} años y tengo una fortuna de {fortune} millones")

# Operaciones con cadenas
x = 10

print(f"The variable is {{x = {x}}}")

"""
Fomrmateando cadenas: Los «f-strings» proporcionan una gran variedad de opciones de formateado: ancho del texto, número de decimales, tamaño de la cifra, alineación, etc.
"""

# Dando formato a valores enteros: d (entero decimal)
mount_height = 3718
print(f"{mount_height:10d}")
print(f"{mount_height:010d}")

# Dando formato a valores flotantes: f (flotante)
PI = 3.14159
print(f"{PI:3f}")
print(f"{PI:.2f}")
print(f"{PI:12f}")
print(f"{PI:7.2f}")
print(f"{PI:07.2f}")
print(f"{PI:010f}")
print(f"{PI:e}")
print(f"{PI:+10.2f}")

"""
Dando formato a cadenas de texto: s (cadena de texto)
"""

text1 = "how"
text2 = "are"
text3 = "you"

print(f"{text1:<7s}|{text2:^11s}|{text3:>7s}")
print(f"{text1:-<7s}|{text2:·^11s}|{text3:->7s}")

"""
Convirtiendo valores enteros a otras bases:
"""

value = 65_321
print(f"{value:b}")
print(f"{value:o}")
print(f"{value:x}")

print(f"{value:07x}")

"""
Modo <<debug>>: Los f-strings permiten imprimir el nombre de la variable y su valor, como un atajo para depurar el código. Para ello se incluye el símbolo = después del nombre de la variable.
"""

serie = "The Big Bang Theory"

imdb_raiting = 8.7

num_seasons = 30

print(f"{serie=}")
print(f"{imdb_raiting=}")
print(f"{serie[4:]=}")
print(f"{imdb_raiting / num_seasons=}")

"""
Modo >>representación>>: Si imprimimos la representación del objeto, tal y como se almacena internamente, podriamos utilizar el modificador '!r' en el f-string. 
"""

name = "Steve Jobs"
is_married = True
print(f"{name!r}")
print(f"{is_married!r}")

"""
Caracteres unicode:
"""
