"""
Archivo: programa_06.py
Autor: Edwin Yoner
Fecha: 25/01/2025

Descripción:
    Este programa solicita un número al usuario y determina si es "Par" o "Impar"
    utilizando el operador módulo (%) y una lista.
"""

# Solicitar al usuario un número entero
num = int(input("Ingrese un número: "))

# Lista que contiene las opciones de paridad
paridad = ["Par", "Impar"]

# Determinar la paridad usando el índice (0 para Par, 1 para Impar)
resultado = paridad[num % 2]

# Mostrar el resultado
print(f"El número {num} es {resultado}.")