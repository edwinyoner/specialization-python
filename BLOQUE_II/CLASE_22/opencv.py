"""
Archivo: opencv.py
Autor: Edwin Yoner
Fecha: 01/03/2025

Descripción:
    Este script muestra cómo utilizar NumPy y OpenCV para manipular imágenes en escala de grises.
    Se realizan las siguientes operaciones:
    - Creación de matrices con `np.zeros()` y `np.ones()`.
    - Modificación de una región específica de la imagen.
    - Visualización de imágenes con OpenCV.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
"""

import numpy as np
import cv2

# Creación de una imagen en escala de grises completamente negra (500x500 píxeles)
imagen_negra = np.zeros((500, 500), dtype=np.uint8)
print("Matriz de imagen negra (500x500):\n", imagen_negra)

# Creación de una imagen en escala de grises completamente blanca (500x500 píxeles)
imagen_blanca = np.ones((500, 500), dtype=np.uint8) * 255
print("Matriz de imagen blanca (500x500):\n", imagen_blanca)

# Creación de una imagen blanca con un rectángulo negro en el centro
imagen_con_cuadro_negro = np.ones((500, 500), dtype=np.uint8) * 255
imagen_con_cuadro_negro[100:400, 100:400] = 0  # Sección central negra

# Mostrar la imagen con OpenCV
cv2.imshow("Imagen con cuadro negro", imagen_con_cuadro_negro)

# Esperar a que el usuario presione una tecla antes de cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
