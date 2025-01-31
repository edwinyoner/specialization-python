"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 16/01/2025

Descripción:
    Este programa explora conceptos fundamentales de Python,
    incluyendo la identidad, tipo y valor de los objetos,
    tipos de datos y operaciones con listas.
"""

# Identidad, Tipo y Valor de los Objetos

x = 10
print(f"x = {x}, id(x) = {id(x)}")

y = x
print(f"y = x, id(y) = {id(y)}")

x = x + 1
print(f"x = x + 1, id(x) = {id(x)}")
print(f"id(y) = {id(y)}")

y = 12
print(f"y = 12, id(y) = {id(y)}")

# Tipos de Datos en Python

x = 10.2
print(f"x = {x}, type(x) = {type(x)}, id(x) = {id(x)}")

y = int(x)
print(f"y = int(x), id(y) = {id(y)}, id(x) = {id(x)}")

x = 5 + 8j
print(f"x = {x}, type(x) = {type(x)}, id(x) = {id(x)}")

# Listas en Python

x = [3, 4, 6, 2, 9, 4, 8]
print(f"x = {x}, type(x) = {type(x)}")

# Cambiando el valor de x a diferentes tipos de datos
x = 2
x = "a"
x = True

# Operaciones con Listas

x = [3, 4, 6, 2, True, 4, 8]
print(f"x = {x}")

# Acceso por índice y slicing
print(f"x[-4] = {x[-4]}")
print(f"x[1:4] = {x[1:4]}")
print(f"x[-6:-3] = {x[-6:-3]}")
print(f"x[4:7] = {x[4:7]}")
print(f"x[-3:] = {x[-3:]}")
print(f"x[0:3] = {x[0:3]}")
print(f"x[3:4] = {x[3:4]}")
print(f"x[3] = {x[3]}")
print(f"x[-4:-3] = {x[-4:-3]}")

# Creación de una lista vacía y su tipo
x = []
print(f"x = {x}, type(x) = {type(x)}")
