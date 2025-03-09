"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 08/03/2025

Descripción:
    Este script crea una imagen en blanco de 500x500 píxeles y dibuja un círculo
    azul en el centro utilizando OpenCV.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
"""

# Importar bibliotecas necesarias
import cv2
import numpy as np

# Mostrar información sobre la función cv2.circle()
help(cv2.circle)

# Crear una imagen en blanco (500x500) con fondo blanco (255,255,255)
imagen = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Definir parámetros del círculo
centro = (250, 250)      # Coordenadas del centro del círculo
radio = 100              # Radio del círculo
color = (255, 0, 0)      # Color azul (en formato BGR)
grosor = -1              # -1 indica que el círculo se rellenará completamente

# Dibujar el círculo en la imagen
cv2.circle(imagen, centro, radio, color, grosor)

# Mostrar la imagen en una ventana
cv2.imshow("Círculo Azul", imagen)

# Esperar a que se presione una tecla antes de cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
