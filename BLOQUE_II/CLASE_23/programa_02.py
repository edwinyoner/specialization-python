"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 03/03/2025

Descripción:
    Este script captura video en tiempo real desde la cámara web y aplica modificaciones en la imagen:
    - Se establece una región específica (100:300, 200:400) en negro.
    - Muestra el video en una ventana en vivo.
    - Se cierra la ventana al presionar la tecla 'a'.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
"""

import cv2

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

    # Modificación del frame: establecer un área rectangular en negro
    frame[100:300, 200:400, :] = 0  # Se asigna negro (0 en los 3 canales)

    # Mostrar el frame en una ventana
    cv2.imshow("Captura de Video Modificada", frame)

    # Salir del bucle si se presiona la tecla 'a'
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# Imprimir información sobre el frame capturado
print("Dimensiones del frame:", frame.shape)
print("Tipo de datos:", frame.dtype)
print("Número de dimensiones:", frame.ndim)

# Liberar los recursos y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
