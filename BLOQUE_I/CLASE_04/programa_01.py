"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 21/01/2025

Descripción:
    Este programa demuestra el uso de tuplas en Python, incluyendo indexación, slicing,
    y la conversión entre tuplas y listas.
"""

# Definición de tuplas
# Las tuplas pueden definirse con o sin paréntesis
x = 2, 7, True, 8, 4  # Definición sin paréntesis
print(x)

x = (2, 7, True, 8, 4)  # Definición con paréntesis (recomendado)
print(x)

# Indexación en tuplas
# Se puede acceder a elementos de la tupla mediante índices positivos y negativos
x = (2, 4, 3, 8, 6, 2)

print(x[0])  # Accede al primer elemento (2)
print(x[-6])  # Accede al primer elemento usando índice negativo (2)

# Slicing en tuplas
# Extrae una subtupla usando el operador de slicing
print(x[1:3])  # Obtiene los elementos desde la posición 1 hasta 2 ([4, 3])

# Conversión de Tupla a Lista
x = (2, 3)  # Tupla original
y = list(x)  # Convierte la tupla en lista
print(y)  # [2, 3]

# Eliminación de un elemento de la lista
y.pop()  # Elimina el último elemento de la lista
print(y)  # [2]

# Conversión de Lista a Tupla
x = tuple(y)  # Convierte la lista de nuevo en tupla
print(x)  # (2,)
