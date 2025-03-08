"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 03/03/2025

Descripción:
    Este script captura video en tiempo real desde la cámara web y lo muestra en una ventana.
    - Usa OpenCV para acceder a la cámara.
    - Muestra el video en una ventana en vivo.
    - Se cierra la ventana al presionar la tecla 'a' (código ASCII 97).

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
"""

import cv2
#help(cv2.VideoCapture)

# Inicializar la captura de video desde la cámara (0 indica la cámara predeterminada)
cap = cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Capturar frame a frame
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo leer el frame.")
        break

    # Mostrar el frame en una ventana
    cv2.imshow("Captura de Video", frame)

    # Salir del bucle si se presiona la tecla 'a' (código ASCII 97)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# Liberar los recursos y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
