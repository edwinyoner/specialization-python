"""
Archivo: operaciones_numpy.py
Autor: Edwin Yoner
Fecha: 27/02/2025

Descripción:
    Este script demuestra operaciones matemáticas básicas con arrays en NumPy, incluyendo:
    - Operaciones aritméticas (+, -, *, /, **, %, //).
    - Producto escalar y producto vectorial entre dos vectores.

Requisitos:
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

import numpy as np

# Definición de listas de números
vector_a = [2, 3, 4]
vector_b = [2, 6, 3]

# Conversión a arrays de NumPy
array_a = np.array(vector_a)
array_b = np.array(vector_b)

# Operaciones básicas entre vectores
suma_vectores = array_a + array_b
resta_vectores = array_a - array_b
multiplicacion_vectores = array_a * array_b
division_vectores = array_a / array_b
potencia_vectores = array_a ** 2  # Eleva cada elemento al cuadrado
modulo_vectores = array_a % array_b  # Módulo (resto de la división)
division_entera_vectores = array_a // array_b  # División entera

# Impresión de resultados
print("Suma de vectores:", suma_vectores)
print("Resta de vectores:", resta_vectores)
print("Multiplicación de vectores:", multiplicacion_vectores)
print("División de vectores:", division_vectores)
print("Potencia de cada elemento en array_a:", potencia_vectores)
print("Módulo (resto de la división):", modulo_vectores)
print("División entera:", division_entera_vectores)

# Producto escalar (dot product)
producto_escalar = np.dot(array_a, array_b)

# Producto vectorial (cross product)
producto_vectorial = np.cross(array_a, array_b)

# Imprimir resultados
print("\nProducto escalar:", producto_escalar)
print("Producto vectorial:", producto_vectorial)
