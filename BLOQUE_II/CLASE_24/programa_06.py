"""
Archivo: programa_06.py
Autor: Edwin Yoner
Fecha: 06/03/2025

Descripción:
    Este script genera un gráfico de línea con una cuadrícula personalizada.
    Se aplican configuraciones de color, grosor, transparencia y estilo de línea a la cuadrícula.

Requisitos:
    - Instalar Matplotlib si no está disponible: `pip install matplotlib`
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

# Importar bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Generar valores aleatorios acumulativos para el eje Y
datos_y = np.random.randn(100).cumsum()

# Definir etiquetas para el eje X (años)
etiquetas_x = ["2010", "2011", "2012", "2013", "2014", "2015"]

# Crear la figura y los ejes
figura, eje = plt.subplots()

# Graficar la serie de datos
eje.plot(datos_y)

# Personalizar la cuadrícula del gráfico
eje.grid(color="orange",      # Color de las líneas de la cuadrícula
         linewidth=1.5,       # Grosor de las líneas
         alpha=0.5,           # Transparencia de la cuadrícula
         linestyle='dotted')  # Estilo de línea punteado

# Mostrar la gráfica
plt.show()
