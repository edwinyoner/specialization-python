"""
Archivo: main.py
Autor: Edwin Yoner
Fecha: 08/02/2025

Descripción:
    Este script principal importa funciones desde los módulos `modulo1.py` y `modulo2.py`
    ubicados en la carpeta `BLOQUE_I/CLASE_12/modulos02/`. 
    Se realizan operaciones matemáticas básicas como suma y resta.
"""

# Importamos los módulos necesarios
from BLOQUE_I.CLASE_12.modulos02 import modulo1 as mod1  # Importamos módulo 1 con alias
import modulo2 as mod2  # Importamos módulo 2 con alias

# Uso de la función suma desde `modulo1`
resultado1 = mod1.suma(5, 10)
print(f"Resultado de la suma (5 + 10): {resultado1}")  # Salida: 15

# Uso de la función resta desde `modulo2`
resultado2 = mod2.resta(10, 20)
print(f"Resultado de la resta (10 - 20): {resultado2}")  # Salida: -10

# Uso de la función suma desde `modulo2`
resultado3 = mod2.suma(10, 20, 30)
print(f"Resultado de la suma (10 + 20 + 30): {resultado3}")  # Salida: -10
