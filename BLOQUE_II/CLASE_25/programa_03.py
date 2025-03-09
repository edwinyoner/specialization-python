"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 08/03/2025

Descripción:
    Este script carga una imagen, aplica un filtro de color utilizando OpenCV
    para generar una máscara basada en un rango de valores RGB, y luego muestra
    la imagen original, la máscara y el resultado de la operación bitwise AND.

Requisitos:
    - Instalar OpenCV si no está disponible: `pip install opencv-python`
    - Asegurar que la imagen "images/circulo.jpg" existe en la ruta correcta.
"""

# Importar bibliotecas necesarias
import cv2
import numpy as np

# Definir el rango de colores a filtrar en formato BGR
color_min = np.array([100, 0, 0])  # Azul mínimo
color_max = np.array([254, 0, 0])  # Azul máximo

# Cargar la imagen
imagen = cv2.imread("images/circulo.jpg")

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
    exit()

# Aplicar un filtro para obtener una máscara con los colores en el rango especificado
mascara = cv2.inRange(imagen, color_min, color_max)

# Aplicar la operación bitwise AND para extraer los píxeles dentro del rango de color
resultado = cv2.bitwise_and(imagen, imagen, mask=mascara)

# Mostrar la imagen original, la máscara y el resultado
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Máscara", mascara)
cv2.imshow("Resultado AND", resultado)

# Obtener las dimensiones de la imagen
alto, ancho, canales = imagen.shape

# Imprimir el valor del píxel en el centro de la imagen
pixel_central = imagen[int(alto / 2), int(ancho / 2)]
print(f"Valor del píxel central: {pixel_central}")

# Esperar a que se presione una tecla antes de cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
