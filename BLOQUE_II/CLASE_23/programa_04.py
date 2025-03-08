"""
Archivo: programa_04.py
Autor: Edwin Yoner
Fecha: 03/03/2025

Descripción:
    Este script crea dos matrices de 2x2 con valores en el rango de 0 a 255 y 
    aplica la operación bitwise AND usando OpenCV.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
"""

import cv2
import numpy as np

# Definir la primera matriz A (2x2)
A = np.array([
    [128, 0],
    [255, 128]
], dtype=np.uint8)

# Definir la segunda matriz B (2x2)
B = np.array([
    [128, 125],
    [255, 255]
], dtype=np.uint8)

# Aplicar la operación bitwise AND entre A y B
C = cv2.bitwise_and(A, B)

# Imprimir matrices y resultado
print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)

print("\nResultado de A AND B:")
print(C)
