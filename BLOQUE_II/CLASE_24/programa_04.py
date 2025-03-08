"""
Archivo: programa_04.py
Autor: Edwin Yoner
Fecha: 06/03/2025

Descripción:
    Este script genera una figura con subgráficos distribuidos en una cuadrícula de 2x3
    utilizando `fig.add_subplot()`. Cada subgráfico muestra una serie de datos aleatorios acumulativos.

Requisitos:
    - Instalar Matplotlib si no está disponible: `pip install matplotlib`
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Generar tres series de datos aleatorios acumulativos
serie_verde = np.random.randn(100).cumsum()
serie_roja = np.random.randn(100).cumsum()
serie_azul = np.random.randn(100).cumsum()  # No se usa, pero puede agregarse en otro subplot

# Crear la figura principal
figura = plt.figure()

# Agregar el primer subgráfico en la posición (2,3,5)
subplot_verde = figura.add_subplot(2, 3, 5)
subplot_verde.plot(serie_verde, color="green")
subplot_verde.set_title("Serie Verde")

# Agregar el segundo subgráfico en la posición (2,3,1)
subplot_rojo = figura.add_subplot(2, 3, 1)
subplot_rojo.plot(serie_roja, color="red")
subplot_rojo.set_title("Serie Roja")

# Mostrar los gráficos
plt.show()
