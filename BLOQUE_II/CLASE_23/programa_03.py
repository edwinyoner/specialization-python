"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 03/03/2025

Descripción:
    Este script carga una imagen en escala de grises y aplica una operación bitwise AND con una matriz de ceros, 
    resaltando una región específica en la imagen.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
    - Asegurarse de que la imagen "mario_bros.jpg" existe en la carpeta "images"
"""

import cv2
import numpy as np

# Cargar la imagen en escala de grises
image = cv2.imread("images/mario_bros.jpg", 0)

# Verificar si la imagen se cargó correctamente
if image is None:
    print("Error: No se pudo cargar la imagen. Verifique la ruta del archivo.")
    exit()

# Crear una matriz de ceros del mismo tamaño que la imagen
zeros = np.zeros(image.shape, dtype=np.uint8)

# Establecer una región específica en blanco (255) dentro de la matriz de ceros
zeros[100:180, 100:180] = 255  # Región blanca en la máscara

# Aplicar operación bitwise AND entre la imagen y la máscara de ceros
bitwise_and_result = cv2.bitwise_and(image, zeros)

# Mostrar las imágenes en ventanas separadas
cv2.imshow("Imagen Original", image)
cv2.imshow("Máscara", zeros)
cv2.imshow("Resultado AND", bitwise_and_result)

# Imprimir información sobre la imagen
print("Dimensiones de la imagen:", image.shape)
print("Tipo de datos:", image.dtype)
print("Número de dimensiones:", image.ndim)

# Esperar a que el usuario presione una tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
