"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 06/03/2025

Descripción:
    Este script genera un gráfico de líneas simple utilizando Matplotlib.
    Se define una serie de valores en el eje Y y se representan en un gráfico 
    con etiquetas y una leyenda.

Requisitos:
    - Instalar Matplotlib si no está disponible: `pip install matplotlib`
"""

# Importamos Matplotlib y su módulo pyplot para la visualización de gráficos
import matplotlib
import matplotlib.pyplot as plt

# Imprimimos la versión de Matplotlib instalada
print(f"Versión de Matplotlib: {matplotlib.__version__}")

# Definir los valores del eje Y
valores_y = [1, 2, 3, 4]

# Crear el gráfico de líneas
plt.plot(valores_y, marker='o', linestyle='-', color='b', label="Valores de muestra")

# Configurar etiquetas de los ejes
plt.xlabel("Índice del dato")
plt.ylabel("Valor del dato")

# Agregar un título al gráfico
plt.title("Gráfico de líneas con Matplotlib")

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico en pantalla
plt.show()