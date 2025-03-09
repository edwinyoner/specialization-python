"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 08/03/2025

Descripción:
    Este script demuestra el uso de la función `cv2.inRange()` para crear una 
    máscara binaria basada en un rango de valores y luego aplicar la operación 
    bitwise AND sobre una matriz de valores.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

# Importar bibliotecas necesarias
import cv2
import numpy as np

# Definir la matriz de entrada (3x3) con valores entre 0 y 255
matriz_original = np.array([
    [10, 50, 200],
    [50, 100, 250],
    [30, 180, 220]
], dtype=np.uint8)

# Definir los valores límite para la operación inRange (rango 100-200)
limite_inferior = 100
limite_superior = 200

# Aplicar la función inRange para generar una máscara binaria
mascara_binaria = cv2.inRange(matriz_original, limite_inferior, limite_superior)

# Aplicar la operación bitwise AND entre la matriz original y la máscara
resultado_and = cv2.bitwise_and(matriz_original, mascara_binaria)

# Imprimir los resultados
print("Matriz Original:")
print(matriz_original)

print("\nMáscara Binaria (Valores en Rango 100-200):")
print(mascara_binaria)

print("\nResultado de Bitwise AND entre Matriz y Máscara:")
print(resultado_and)
