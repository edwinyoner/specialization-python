"""
Archivo: numpy_arrays.py
Autor: Edwin Yoner
Fecha: 27/02/2025

Descripción:
    Este script demuestra el uso de arrays en NumPy, incluyendo:
    - Creación de vectores y matrices con diferentes tipos de datos.
    - Acceso a elementos mediante indexación.
    - Uso de slicing (rebanado) para extraer submatrices.
    - Exploración de atributos como dimensiones, forma y tipo de datos.

Requisitos:
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

import numpy as np

# Definición de un vector unidimensional como lista de Python
lista_numeros = [2, 3, 4]

# Definición de una matriz bidimensional como lista de listas
matriz_numeros = [
    [4, 6, 3, 4],
    [1, 2, 7, 2],
    [9, 4, 7, 1],
    [6, 4, 0, 2]
]

# Convertir la lista en un array de NumPy con tipo de dato int16
vector_numpy = np.array(lista_numeros, dtype=np.int16)
print("Vector (NumPy):")
print(vector_numpy)

# Convertir la lista de listas en una matriz NumPy con tipo uint8
matriz_numpy = np.array(matriz_numeros, dtype=np.uint8)
print("\nMatriz (NumPy):")
print(matriz_numpy)

# Atributos de los arrays
print("\nAtributos del vector:")
print(f"Dimensiones: {vector_numpy.ndim}, Forma: {vector_numpy.shape}, Tipo de datos: {vector_numpy.dtype}")

print("\nAtributos de la matriz:")
print(f"Dimensiones: {matriz_numpy.ndim}, Forma: {matriz_numpy.shape}, Tipo de datos: {matriz_numpy.dtype}")

# Indexación en listas normales
print("\nIndexación en la lista original:")
print(f"Elemento en la posición 1: {lista_numeros[1]}, Elemento penúltimo: {lista_numeros[-2]}")

# Indexación en la matriz bidimensional
print("\nIndexación en la lista de listas original:")
print(f"Elemento en b[0][1]: {matriz_numeros[0][1]}, Elemento en b[3][0]: {matriz_numeros[3][0]}")

# Indexación en la matriz NumPy
print("\nIndexación en la matriz NumPy:")
print(f"Elemento en m[0,1]: {matriz_numpy[0,1]}, Elemento en m[3,0]: {matriz_numpy[3,0]}")

# Slicing (rebanado) en la matriz NumPy
print("\nSubmatrices extraídas con slicing:")

# Extraer una fila y dos columnas específicas
print("Filas 1 a 2, Columnas 1 a 3:\n", matriz_numpy[1:2, 1:3])

# Extraer varias filas y columnas
print("Filas 1 a 4, Columnas 1 a 3:\n", matriz_numpy[1:4, 1:3])

# Obtener todas las filas desde la posición 0 y todas las columnas desde la posición 1
print("Todas las filas, columnas desde la segunda:\n", matriz_numpy[0:, 1:])

# Extraer la última fila y solo una columna específica
print("Última fila, segunda columna:\n", matriz_numpy[3:, 1:2])
