"""
Archivo: main.py
Autor: Edwin Yoner
Fecha: 08/02/2025

Descripción:
    Este script importa funciones del módulo `mod_ejercicios.py` y las utiliza
    para calcular potencias y sumar elementos de una lista de manera recursiva.
"""

# Importación de funciones desde el módulo personalizado
from mod_ejercicios import *

# Cálculo de potencia
base, exponente = 2, 5
print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")  # Salida: 32

# Definición de una lista
s = [2, 3, 4, 1, 0, 5]

# Cálculo de la suma de los elementos de la lista
print("Suma de la lista:", suma_recursiva_lista(s))  # Salida: 15
