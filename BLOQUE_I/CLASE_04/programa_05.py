"""
Archivo: programa_05.py
Autor: Edwin Yoner
Fecha: 21/01/2025

Descripción:
    Este programa muestra cómo manipular strings dentro de una lista en Python,
    utilizando el método upper() para convertir cada string a mayúsculas.
"""

# Lista de países en minúsculas
x = ["peru", "ecuador", "argentina"]

# Convertir cada elemento de la lista a mayúsculas usando upper()
x[0] = x[0].upper()
x[1] = x[1].upper()
x[2] = x[2].upper()

# Imprimir la lista modificada
print(x)  # Salida: ['PERU', 'ECUADOR', 'ARGENTINA']