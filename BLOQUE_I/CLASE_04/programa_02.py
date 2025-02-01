"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 21/01/2025

Descripción:
    Este programa demuestra el uso de métodos en tuplas en Python,
    incluyendo count() para contar ocurrencias y index() para encontrar la posición de un elemento.
"""

# Definición de una tupla con valores repetidos
x = (2, 3, 4, 4, 4, 5)

# Método count(): Cuenta cuántas veces aparece un valor en la tupla
repeticiones = x.count(4)
print(f"El número 4 aparece {repeticiones} veces en la tupla.")  # Salida: 3

# Método index(): Encuentra la primera aparición de un valor en la tupla
posicion = x.index(4)
print(f"El primer número 4 se encuentra en la posición {posicion}.")  # Salida: 2
