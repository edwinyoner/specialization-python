"""
Archivo: programa_05.py
Autor: Edwin Yoner
Fecha: 06/03/2025

Descripción:
    Este script genera un gráfico de línea que representa las ventas proyectadas para el año 2025.
    Se personalizan los títulos, etiquetas de ejes y los valores del eje X con etiquetas de años.

Requisitos:
    - Instalar Matplotlib si no está disponible: `pip install matplotlib`
    - Instalar NumPy si no está disponible: `pip install numpy`
"""

# Importar bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Definir valores del eje X (rango de 100 a 200)
eje_x = range(100, 200)

# Generar valores aleatorios acumulativos para el eje Y
ventas_acumuladas = np.random.randn(100).cumsum()

# Definir etiquetas para los valores del eje X (años)
etiquetas_x = ["2010", "2011", "2012", "2013", "2014", "2015"]

# Crear la figura y los ejes
figura, eje = plt.subplots()

# Graficar la serie de datos
eje.plot(eje_x, ventas_acumuladas)

# Personalizar título y etiquetas de los ejes
eje.set_title("Ventas 2025", fontsize=20, color="orange")
eje.set_xlabel("Años", color="red")
eje.set_ylabel("Dólares", color="green")

# Personalizar las etiquetas del eje X
eje.set_xticks(range(120, 180, 10))  # Definir la posición de las marcas en el eje X
eje.set_xticklabels(etiquetas_x)  # Asignar etiquetas personalizadas

# Mostrar la gráfica
plt.show()
