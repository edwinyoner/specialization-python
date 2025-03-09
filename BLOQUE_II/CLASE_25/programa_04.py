"""
Archivo: programa_04.py
Autor: Edwin Yoner
Fecha: 08/03/2025

Descripción:
    Este script carga un video, convierte cada fotograma a HSV,
    aplica una máscara para detectar objetos dentro de un rango de color
    específico y guarda capturas cuando se detectan suficientes píxeles blancos.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
    - Asegurar que el archivo "video/circles.avi" existe en la ruta correcta.
"""

# Importar bibliotecas necesarias
import cv2
import numpy as np

# Cargar el video
video = cv2.VideoCapture("video/circles.avi")

# Definir el rango de color en formato HSV (para detectar el objeto)
color_min = np.array([110, 80, 80])   # Mínimo (H, S, V)
color_max = np.array([120, 255, 255]) # Máximo (H, S, V)

# Contador de imágenes guardadas
contador_fotos = 0

# Definir el umbral de detección (cantidad de píxeles blancos necesarios para considerar un objeto detectado)
umbral_pixeles = 15000

# Bucle para procesar cada fotograma del video
while video.isOpened():
    # Leer el siguiente fotograma
    ret, frame = video.read()

    # Verificar si el fotograma se leyó correctamente
    if not ret:
        break

    # Convertir el fotograma de BGR a HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear la máscara de color
    mascara = cv2.inRange(frame_hsv, color_min, color_max)

    # Aplicar la operación bitwise AND para extraer el objeto detectado
    resultado = cv2.bitwise_and(frame, frame, mask=mascara)

    # Contar los píxeles blancos en la máscara
    cantidad_pixeles_blancos = cv2.countNonZero(mascara)

    # Verificar si se detecta el objeto (según el umbral de píxeles blancos)
    if cantidad_pixeles_blancos > umbral_pixeles:
        print("🔹 Objeto Detectado")
        nombre_imagen = f"images/foto{contador_fotos}.jpg"
        cv2.imwrite(nombre_imagen, frame)  # Guardar la imagen del fotograma
        print(f"📷 Imagen guardada: {nombre_imagen}")
        contador_fotos += 1

    # Mostrar los resultados en ventanas
    cv2.imshow("Video Original", frame)
    cv2.imshow("Máscara de Color", mascara)
    cv2.imshow("Detección AND", resultado)

    # Esperar 120 ms entre fotogramas y salir si se presiona la tecla 'a'
    if cv2.waitKey(120) == ord('a'):
        break

# Liberar recursos y cerrar ventanas
video.release()
cv2.destroyAllWindows()
