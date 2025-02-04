"""
Archivo: programa_08.py
Autor: Edwin Yoner
Fecha: 28/01/2025

Descripción:
    Este programa imprime un patrón cuadrado de asteriscos (*) utilizando bucles anidados `while`.
"""

# Definir el número de filas y columnas del cuadrado
filas = 4
columnas = 4

# Bucle externo para controlar las filas
i = 1
while i <= filas:
    j = 1  # Reinicia la variable `j` en cada nueva fila
    while j <= columnas:
        print("*", end=" ")  # Imprime el asterisco sin salto de línea
        j += 1
    print("")  # Salto de línea para pasar a la siguiente fila
    i += 1