"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 06/03/2025

Descripción:
    Este script genera gráficos utilizando Matplotlib y NumPy.
    Se crean múltiples configuraciones de subgráficos (`subplots`)
    y se visualiza una serie de datos aleatorios acumulativos.

Requisitos:
    - Instalar Matplotlib si no está disponible: `pip install matplotlib`
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Generar una serie de datos aleatorios acumulativos
datos_acumulativos = np.random.randn(100).cumsum()

# Crear una figura con un solo subgráfico
figura, ejes = plt.subplots()

# Crear una figura con una cuadrícula de 2x2 subgráficos
figura, ejes = plt.subplots(2, 2)

# Crear una figura con una cuadrícula de 2x2 subgráficos compartiendo ejes X e Y
figura, ejes = plt.subplots(2, 2, sharex=True, sharey=True)

# Ajustar el tamaño de la figura
figura.set_size_inches(9, 9)

# Imprimir información sobre la figura y los ejes
print(figura, ejes)

# Graficar los datos en el subgráfico ubicado en la posición (1,0)
ejes[1, 0].plot(datos_acumulativos)

# Mostrar los gráficos
plt.show()
