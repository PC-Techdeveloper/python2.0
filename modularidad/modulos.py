"""
Los módulos son simplemente ficheros de texto que contienen código Python y representan unidades con las que evitar la repetición de código y favorecer la reutilización de código.
"""

# Importar un módulo completo:
# import stats

""" print(
    stats.mean(
        6,
        3,
        9,
        5,
    )
)

print(stats.std(2, 4, 8)) """

"""
Importar partes de un módulo:
"""

# from stats import mean

# result = mean(6, 3, 9, 4)

# print(result)

# Importar varios objetos en un mismo módulo:
# from stats import mean, std

# from stats import *  # Importar todos los objetos

"""
Importar usando un alias: Usar un nombre diferente del módulo u objeto para importarlo mejora la legibilidad de nuestro código.
"""

# from stats import mean as avg

# print(avg(6, 3, 9, 12))

"""
Paquetes:
Un paquete es una carpeta que contiene ficheros de Python y otros paquetes.
"""

# Importar desde un paquete:

from extramath import frac, stats
print(frac.gcd(21, 35))
print(stats.mean(6, 3, 9, 12))

"""
Programa principal:
El programa principal es el fichero que se englobará en paquetes y existirá uno en concreto que será el punto de entrada, también llamado programa principal.

La variable __name__ toma los siguientes valores:
- El nombre del módulo (o paquete) al importar el fichero.
- El valor '__main__' cuando se ejecuta el fichero como un programa.
"""

# ESTRUCTURA:

# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios

# CÓDIGO PROPIO
# ...
# CÓDIGO PROPIO

""" if __name__ == "__main__":
    # Este código se ejecutará cuando se ejecute el programa
    print("Punto de entrada del programa")
"""

# import blabla


# def myFunc():
#    print("Inside myFunc")
#    blabla.hi()


# if __name__ == "__main__":
#    print("Entry point")
#    myFunc()
