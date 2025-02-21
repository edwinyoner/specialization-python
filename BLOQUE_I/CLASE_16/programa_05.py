"""
Archivo: programa_05.py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este programa maneja los errores comunes al realizar operaciones de división,
    incluyendo la división por cero (`ZeroDivisionError`) y el uso incorrecto de tipos de datos (`TypeError`).
"""

# 1. Manejo de ZeroDivisionError
try:
    x = 0
    resultado = 10 / x
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except TypeError:
    print("Error: Solo se puede dividir entre números.")

# 2. Manejo de TypeError
try:
    x = "3"  # Intento de dividir un número entre una cadena
    resultado = 10 / x
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except TypeError:
    print("Error: Solo se puede dividir entre números.")

# 3. Manejo combinado de errores con tuple
try:
    x = "3"
    resultado = 10 / x
except (ZeroDivisionError, TypeError):
    print("Error: Dato ingresado no válido para la división.")
except Exception as e:
    print(f"Error inesperado ({type(e).__name__}): {e}")  # Muestra el tipo de error inesperado

