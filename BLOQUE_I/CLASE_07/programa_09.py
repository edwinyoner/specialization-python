"""
Archivo: programa_09.py
Autor: Edwin Yoner
Fecha: 28/01/2025

Descripción:
    Este programa genera patrones de asteriscos (*) utilizando bucles `while`.
    Se imprimen dos tipos de figuras:
    1. Un triángulo creciente.
    2. Un triángulo invertido.
"""

# Triángulo creciente
print("Triángulo creciente:")
n = 3  # Número de filas
i = 0
while i <= n:
    print("* " * (i + 1))  # Imprime `i+1` asteriscos en cada fila
    i += 1
print(" ")  # Espacio entre figuras

# Triángulo invertido
print("Triángulo invertido:")
n = 4  # Número de filas
i = 1
while i <= n:
    print("* " * n)  # Imprime `n` asteriscos en cada fila
    n -= 1  # Reduce el número de asteriscos en la siguiente fila

print(" ")  # Espacio final