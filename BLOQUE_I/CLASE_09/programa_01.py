"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 01/02/2025

Descripción:
    Este programa genera diferentes patrones de asteriscos (*) utilizando bucles `for`
    y también calcula el factorial de un número dado.
"""

# Triángulo rectángulo creciente
print("Triángulo rectángulo creciente:")
for i in range(4):
    print("* " * (i + 1))

print("\n")

# Triángulo rectángulo invertido
print("Triángulo rectángulo invertido:")
n = 4
for i in range(n):
    print("* " * n)
    n -= 1

print("\n")

# Pirámide alineada a la derecha
print("Pirámide alineada a la derecha:")
n = 4
for i in range(n):
    print("  " * (n - i) + "* " * (i + 1))

print("\n")

# Pirámide con mayor espaciado
print("Pirámide con mayor espaciado:")
n = 3
for i in range(n):
    print("  " * (n - i) + "  * " * (i + 1))

print("\n")

# Cálculo del factorial de un número
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial de {n}: {fact}")