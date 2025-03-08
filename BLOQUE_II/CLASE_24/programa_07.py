"""
Archivo: programa_07.py
Autor: Edwin Yoner
Fecha: 06/03/2025

Descripción:
    Este script genera un gráfico de línea con una cuadrícula personalizada en un fondo oscuro.
    Se configuran diferentes estilos de cuadrícula para los ejes X e Y, diferenciando entre
    líneas principales y secundarias.

Requisitos:
    - Instalar Matplotlib si no está disponible: `pip install matplotlib`
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

# Importar bibliotecas necesarias
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

# Generar datos aleatorios acumulativos para el eje Y
datos_y = np.random.randn(100).cumsum()

# Definir etiquetas para el eje X (años)
etiquetas_x = ["2010", "2011", "2012", "2013", "2014", "2015"]

# Aplicar estilo de fondo oscuro
plt.style.use('dark_background')

# Crear la figura y los ejes
figura, eje = plt.subplots()

# Graficar la serie de datos
eje.plot(datos_y, label="Consumo", color="cyan")  # Línea de color cyan para mejor visibilidad
eje.legend()  # Mostrar leyenda

# Configuración del eje X
eje.xaxis.set_major_locator(MultipleLocator(10))  # Ubicación de ticks principales cada 10 unidades
eje.xaxis.set_minor_locator(MultipleLocator(2))   # Ubicación de ticks secundarios cada 2 unidades
eje.grid(which="major", axis="x", color="steelblue")  # Cuadrícula principal en azul acero
eje.grid(which="minor", axis="x", color="orange", alpha=0.5)  # Cuadrícula secundaria en naranja con transparencia

# Configuración del eje Y
eje.yaxis.set_major_locator(MultipleLocator(2))  # Ubicación de ticks principales cada 2 unidades
eje.yaxis.set_minor_locator(MultipleLocator(1))  # Ubicación de ticks secundarios cada 1 unidad
eje.grid(which="major", axis="y", color="red")   # Cuadrícula principal en rojo
eje.grid(which="minor", axis="y", color="green", alpha=0.5)  # Cuadrícula secundaria en verde con transparencia

# Mostrar la gráfica
plt.show()
