"""
Lectura de un fichero:

* Python ofrece la función open() para abrir un fichero. Esta apertura se puede realizar en 3 modos distintos: Lectura, Escritura y Añadido.
"""

# Primero abrir el fichero
# Primer argumento: Ruta al fichero
# Segundo argumento: Modo de apertura
f = open("./files/temps.txt", "r")

"""
Lectura completa de un fichero

* read(): Devuelve todo el contenido del fichero como una cadena de texto (str).
* readLines(): Devuelve todo el contenido del fichero como una lista (list) donde cada línea es un elemento de la lista.
"""

print(f.read())
print(f.readlines())
