"""
Archivo: main.py
Autor: Edwin Yoner
Fecha: 11/02/2025

Descripción:
    Este módulo importa la clase Operacion desde el módulo operacion3 
    y realiza operaciones matemáticas de suma.
"""

# Importación del módulo operacion3
import operacion3

# Creación de una instancia de la clase Operacion con valores 5 y 5
op3 = operacion3.Operacion(5, 5)

# Impresión del resultado de la suma
print(f'La suma es = {op3.sumar()}')

# Código comentado de importación alternativa con importación global de Operacion
"""
from operacion3 import *

op2 = Operacion(3, 4)
print(op2.sumar())
"""
