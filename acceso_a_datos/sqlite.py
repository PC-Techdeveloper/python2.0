"""
Conexión a la base de datos SQLite:

La conexión a la base de datos se realiza a través de la función connect()
que espera recibir la ruta de fichero de base de datos y devuelve un objeto de tipo Connection.
"""

import sqlite3

connection = sqlite3.connect("python.db")

print("Conexión a la base de datos SQLite establecida", connection)

"""
Crear un cursor: Se podría ver como un manejador para realizar operaciones sobre la base de datos.
"""

cur = connection.cursor()

print("Cursor creado", cur)

"""
Creación de tablas:	
"""

slq = """CREATE TABLE pyversions (
  branch TEXT PRIMARY KEY,
  released_at_year INTEGER,
  released_at_month INTEGER,
  release_manager TEXT,
)"""

print(cur.execute(slq))
