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
# f = open("./files/temps.txt", "r")


# print(f.read())
# print(f.readlines())

# Lectura línea a línea
""" for line in f:
    print(line)
 """
# Lectura de una línea
""" for line in f:
    print(line)
    break
 """
# Python ofrece la función readline()
file = f.readline()
# print(file)

## Lectura de las 3 primeras lineas
""" for _ in range(3):
    print(f.readline().strip())
 """
## Lectura de las restantes lineas
""" for line in f:
    print(line.strip())
 """
# seek(): Permite moverse a una determinada posición en el fichero
f = open("./files/temps.txt")

for line in f:
    print(line.strip(), end=" ")

f.seek(0)  # Posición inicial

for line in f:
    print(line.strip(), end=" ")

"""
Enumerando líneas:
"""
for line_no, line in enumerate(f):
    print(f"Línea {line_no}: {line.strip()}")

"""
Escritura en un fichero:
Para escribir texto en un fichero hay que abrir dicho fichero en MODO ESCRITURA. Para ello se utiliza el argumento adicional en la función open() que indica esta operación.
"""

# Abrir el fichero

f = open("./files/temps.txt", "w")

# write(): Escribe una cadena de texto en el fichero

canary_iata = ("TFN", "TFS", "LPA", "GMZ", "VDE", "SPC", "ACE", "FUE")

# Añadir el salto de línea de manera explicita

# f.write("\n".join(canary_iata))

f.writelines("\n".join(canary_iata))

f.close()  # Cerrar el fichero

"""
Añadir a un fichero: Función append() / a
"""
f = open("./files/more.txt", "a")

"""
Usando contextos: 
* with y el contexto creado se ocupará de cerrar adecuadamente el fichero.
"""

with open("files/temps.txt") as f:
    for line in f:
        min_temp, max_temp = line.strip().split()
        print(min_temp, max_temp)
