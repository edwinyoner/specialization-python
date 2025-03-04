"""
Archivo: numpy_arrays.py
Autor: Edwin Yoner
Fecha: 01/03/2025

Descripción:
    Este script muestra cómo trabajar con arrays de NumPy utilizando funciones como:
    - `np.zeros()` para crear matrices de ceros.
    - `np.ones()` para crear matrices de unos.
    - `np.arange()` para generar secuencias numéricas con diferentes parámetros.
    - Operaciones aritméticas con arrays.

Requisitos:
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

import numpy as np

# Creación de un vector a partir de una lista
lista_numeros = [1, 55]
vector_numeros = np.array(lista_numeros, dtype=np.uint8)
print("Vector a partir de lista:", vector_numeros)

# Creación de una matriz de ceros (5x5)
matriz_ceros = np.zeros((5, 5), dtype=np.uint8)
print("\nMatriz de ceros (5x5):\n", matriz_ceros)

# Sumar un escalar a la matriz de ceros
print("\nMatriz de ceros + 5:\n", matriz_ceros + 5)
print("\nMatriz de ceros + 255 (saturado en uint8):\n", matriz_ceros + 255)

# Creación de una matriz de unos (2x2)
matriz_unos = np.ones((2, 2), dtype=np.uint8)
print("\nMatriz de unos (2x2):\n", matriz_unos)

# Uso de np.arange() para generar secuencias numéricas
secuencia_simple = np.arange(2, 10)
print("\nSecuencia del 2 al 9:", secuencia_simple)

secuencia_saltos = np.arange(2, 20, 3)
print("\nSecuencia del 2 al 19 con salto de 3:", secuencia_saltos)

# Uso de reshape() para cambiar la forma de un array
matriz_secuencia = np.arange(0, 20).reshape(5, 4)
print("\nMatriz 5x4 generada con np.arange():\n", matriz_secuencia)
