"""
Archivo: main.py
Autor: Edwin Yoner
Fecha: 08/02/2025

Descripción:
    Este script principal importa funciones de los módulos `modulo1.py` y `modulo2.py`
    para realizar operaciones matemáticas básicas como suma, resta y multiplicación.
"""

# Importamos las funciones necesarias desde los módulos
from modulo1 import suma as suma_dos_numeros #from modulo1 import *
from modulo2 import suma as suma_tres_numeros, resta, multiplicacion

# Definimos valores de prueba
a, b, c = 10, 5, 2

# Realizamos operaciones utilizando las funciones importadas
resultado_suma_2 = suma_dos_numeros(a, b)
resultado_suma_3 = suma_tres_numeros(a, b, c)
resultado_resta = resta(a, b)
resultado_multiplicacion = multiplicacion(a, b)

# Mostramos los resultados en consola
print(f"Suma de {a} y {b}: {resultado_suma_2}")  # Salida: 15
print(f"Suma de {a}, {b} y {c}: {resultado_suma_3}")  # Salida: 17
print(f"Resta de {a} y {b}: {resultado_resta}")  # Salida: 5
print(f"Multiplicación de {a} y {b}: {resultado_multiplicacion}")  # Salida: 50
