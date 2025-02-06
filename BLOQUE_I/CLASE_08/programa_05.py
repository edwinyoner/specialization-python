"""
Archivo: programa_05.py
Autor: Edwin Yoner
Fecha: 30/01/2025

Descripción:
    Este programa muestra cómo utilizar estructuras por comprensión en Python 
    para la generación de tuplas.
"""

# Creación de una tupla de números de 0 a 7 (Versión tradicional)
a = (0, 1, 2, 3, 4, 5, 6, 7)
print("Tupla original:", a)

# Generación de una tupla usando comprensión de tuplas
a_comp = tuple(x for x in range(8))
print("Tupla generada con comprensión:", a_comp)

# Generación de una tupla usando tuple()
a_list = tuple(range(8))
print("Tupla generada con tuple():", a_list)