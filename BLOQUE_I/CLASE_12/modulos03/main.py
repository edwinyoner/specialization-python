"""
Archivo: main.py
Autor: Edwin Yoner
Fecha: 08/02/2025

Descripción:
    Este script principal importa la función `suma` desde el módulo `modulo1.py`.
    Se realiza una operación de suma y se introduce un retardo en la ejecución con `time.sleep(5)`.
"""

# Importación de módulos
import modulo1  # Importamos nuestro módulo personalizado
import time  # Importamos la librería `time` para introducir pausas en la ejecución

# Uso de la función `suma` desde `modulo1`
resultado = modulo1.suma(2, 7)
print(f"Resultado de la suma (2 + 7): {resultado}")  # Salida: 9

# Introducimos un retardo de 5 segundos antes de imprimir nuevamente el resultado
time.sleep(5)
print(f"Resultado después de 5 segundos: {resultado}")

# Comentarios y exploración de módulos
# print(__name__)  # Verifica si el script se ejecuta como principal
# help(time)  # Muestra la documentación del módulo time

# Ejemplo de importación de librerías (comentadas)
"""
import numpy as np
import cv2  # OpenCV para procesamiento de imágenes
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import QLabel  # Cambio en la importación correcta de PyQt5
import pymysql  # Conexión con bases de datos MySQL
"""