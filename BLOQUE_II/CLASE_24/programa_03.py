"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 06/03/2025

Descripción:
    Este script genera dos gráficos en la misma figura utilizando Matplotlib.
    Se usa `plt.axes()` para posicionar manualmente un gráfico dentro de otro.

Requisitos:
    - Instalar Matplotlib si no está disponible: `pip install matplotlib`
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Generar dos series de datos aleatorios acumulativos
serie_principal = np.random.randn(100).cumsum()
serie_secundaria = np.random.randn(100).cumsum()

# Crear una figura principal
figura = plt.figure()

# Crear el primer eje (gráfico principal)
eje_principal = plt.axes()
eje_principal.plot(serie_principal, label="Serie Principal", color="blue")
eje_principal.legend()

# Crear un segundo eje (gráfico superpuesto en una posición específica)
eje_secundario = plt.axes([0, 0, 0.5, 0.5])  # [x, y, ancho, alto] en coordenadas normalizadas
eje_secundario.plot(serie_secundaria, label="Serie Secundaria", color="orange")
eje_secundario.legend()

# Mostrar los gráficos
plt.show()
