"""
Archivo: programa_07.py
Autor: Edwin Yoner
Fecha: 28/01/2025

Descripción:
    Este programa utiliza bucles `while` para mostrar números en diferentes formatos:
    1. Imprime los números del 0 al 10.
    2. Imprime solo los números pares del 0 al 10.
    3. Imprime el cuadrado de los números pares del 0 al 10.
"""

# Imprimir números del 0 al 10
numero = 10
iteracion = 0
while iteracion <= numero:
    print(iteracion, end="  ")  # Se imprimen los números de 0 a 10 en una sola línea
    iteracion += 1
print("\n")  # Salto de línea para separar los resultados

# Imprimir solo los números pares del 0 al 10
iteracion = 0
while iteracion <= numero:
    if iteracion % 2 == 0:  # Verifica si el número es par
        print(iteracion, end="  ")
    iteracion += 1
print("\n")  # Salto de línea para separar los resultados

# Imprimir el cuadrado de los números pares del 0 al 10
iteracion = 0
while iteracion <= numero:
    if iteracion % 2 == 0:  # Verifica si el número es par
        print(iteracion ** 2, end="  ")  # Se imprime el cuadrado del número
    iteracion += 1
print("\n")  # Salto de línea final