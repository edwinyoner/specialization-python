"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 18/01/2025

Descripción:
    Este programa demuestra el uso de listas en Python, incluyendo acceso a elementos anidados,
    obtención de la longitud de una lista y el uso de slicing en listas anidadas.
"""

# Definimos una lista con diferentes tipos de datos, incluyendo otra lista dentro de ella
x = [True, None, [3, 2, 1, 4, 8], 9, False]

# Imprimimos la lista completa
print("Lista completa:", x)

# Imprimimos la cantidad de elementos en la lista
print("Longitud de la lista:", len(x))

# Accedemos a un elemento dentro de la lista anidada
print("Elemento en la posición [2][1]:", x[2][1])  # Accede al segundo elemento de la lista interna

# Accedemos a un elemento de la lista principal
print("Elemento en la posición [1]:", x[1])  # Devuelve None

# Aplicamos slicing en la lista anidada (extrae elementos del índice 1 al 3)
print("Sublista de la lista anidada [1:4]:", x[2][1:4])  

# Accedemos a un subconjunto específico de la lista anidada
print("Elemento en la posición [3:4] de la lista anidada:", x[2][3:4])

# Extraemos toda la lista interna usando slicing
print("Lista interna completa:", x[2][:])
