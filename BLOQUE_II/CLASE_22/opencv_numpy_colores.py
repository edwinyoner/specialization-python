"""
Archivo: opencv_numpy_colores.py
Autor: Edwin Yoner
Fecha: 01/03/2025

Descripción:
    Este script demuestra cómo crear y visualizar una imagen en color con NumPy y OpenCV.
    - Se genera una imagen de 2x2 píxeles con color blanco.
    - Se visualiza la imagen en una ventana con OpenCV.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
"""

import numpy as np
import cv2

# Crear una imagen de 2x2 píxeles en color (RGB) completamente blanca
imagen_blanca = np.ones((2, 2, 3), dtype=np.uint8) * 255
print("Matriz de imagen blanca (2x2 píxeles en RGB):\n", imagen_blanca)

# Mostrar la imagen en una ventana con OpenCV
cv2.imshow("Imagen Blanca", imagen_blanca)

# Esperar a que el usuario presione una tecla antes de cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()