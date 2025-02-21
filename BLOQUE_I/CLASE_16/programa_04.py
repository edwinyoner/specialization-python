"""
Archivo: programa_04.py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este programa maneja el error TypeError cuando se intenta realizar una operación
    no permitida entre diferentes tipos de datos.
"""

try:
    # Intento de sumar un entero y una cadena (esto generará TypeError)
    resultado = 15 + "12"

except TypeError:
    print("Error: No se puede sumar un número entero con una cadena de texto. Verifique los tipos de datos.")

except Exception as e:  # Captura cualquier otro error inesperado
    print(f"Error inesperado: {e}")

finally:
    print("Operación finalizada.")
