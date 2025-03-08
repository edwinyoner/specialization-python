"""
Archivo: programa_05.py
Autor: Edwin Yoner
Fecha: 03/03/2025

Descripción:
    - Este script carga una imagen en color y aplica una máscara binaria.
    - La máscara tiene una región blanca en el centro que permite visualizar 
      solo una parte de la imagen original mediante la operación bitwise AND.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
    - Asegurar que la imagen "mario_bros.jpg" está en la carpeta "images/"
"""

import cv2
import numpy as np

# Cargar la imagen en color
imagen = cv2.imread("images/mario_bros.jpg", 1)

# Validar que la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
    exit()

# Crear una matriz de ceros (máscara binaria)
altura, ancho = imagen.shape[:2]  # Obtener dimensiones de la imagen
mascara = np.zeros((altura, ancho), dtype=np.uint8)  # Máscara del tamaño de la imagen

# Definir una región blanca en la máscara
mascara[100:180, 100:180] = 255  # Solo esta zona permitirá ver la imagen

# Aplicar la operación bitwise AND usando la máscara
resultado = cv2.bitwise_and(imagen, imagen, mask=mascara)

# Mostrar las imágenes
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Máscara Binaria", mascara)
cv2.imshow("Resultado AND con Máscara", resultado)

# Imprimir detalles de la imagen
print(f"Dimensiones de la imagen: {imagen.shape}")
print(f"Tipo de datos: {imagen.dtype}")
print(f"Número de dimensiones: {imagen.ndim}")

# Esperar una tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
