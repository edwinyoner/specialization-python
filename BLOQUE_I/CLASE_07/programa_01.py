"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 28/01/2025

Descripción:
    Este programa demuestra el uso de operadores lógicos en Python,
    incluyendo AND, NOT y comparaciones lógicas avanzadas.
"""

# Definición de valores booleanos
a = True
b = False

# Uso del método interno __and__()
resultado_and_metodo = a.__and__(b)  # Uso del método especial de AND
print(f"Resultado de a.__and__(b): {resultado_and_metodo}")

# Uso del operador lógico AND
resultado_and = a and b
print(f"Resultado de a and b: {resultado_and}")

# Uso del operador NOT
resultado_not = not resultado_and
print(f"Resultado de not(a and b): {resultado_not}")

# Expresión lógica combinada con comparaciones
resultado_expresion = not((a > b) and (b != a))
print(f"Resultado de not((a > b) and (b != a)): {resultado_expresion}")