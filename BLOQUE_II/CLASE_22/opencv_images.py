"""
Archivo: opencv_images.py
Autor: Edwin Yoner
Fecha: 01/03/2025

Descripción:
    Este script carga una imagen desde el disco y muestra sus canales de color (BGR) de forma individual.
    - Se carga la imagen usando OpenCV.
    - Se muestran los canales Azul (B), Verde (G) y Rojo (R) por separado.
    - Se eliminan progresivamente los canales de color para observar los efectos.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
    - Asegurarse de que la imagen `images/img.png` existe en la ruta especificada.
"""

import numpy as np
import cv2

# Cargar la imagen en formato BGR
ruta_imagen = "images/img.png"
imagen = cv2.imread(ruta_imagen)

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print(f"Error: No se pudo cargar la imagen en '{ruta_imagen}'. Verifica la ruta.")
    exit()

# Mostrar información sobre la imagen
print(f"Dimensiones de la imagen: {imagen.shape}")  # (altura, ancho, canales)

# Mostrar la imagen original
cv2.imshow("Imagen Original", imagen)

# Mostrar los canales de color individualmente
cv2.imshow("Canal Azul (B)", imagen[:, :, 0])
cv2.imshow("Canal Verde (G)", imagen[:, :, 1])
cv2.imshow("Canal Rojo (R)", imagen[:, :, 2])

# Eliminar el canal azul y mostrar la imagen resultante
imagen_sin_azul = imagen.copy()
imagen_sin_azul[:, :, 0] = 0
cv2.imshow("Imagen sin Azul", imagen_sin_azul)

# Eliminar el canal verde y mostrar la imagen resultante
imagen_sin_verde = imagen.copy()
imagen_sin_verde[:, :, 1] = 0
cv2.imshow("Imagen sin Verde", imagen_sin_verde)

# Eliminar el canal rojo y mostrar la imagen resultante
imagen_sin_rojo = imagen.copy()
imagen_sin_rojo[:, :, 2] = 0
cv2.imshow("Imagen sin Rojo", imagen_sin_rojo)

# Esperar a que el usuario presione una tecla antes de cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
