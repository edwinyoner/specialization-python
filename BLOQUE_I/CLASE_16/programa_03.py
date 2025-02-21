"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este programa maneja el error KeyError cuando se intenta acceder a una clave
    que no existe en un diccionario.
"""

try:
    # Diccionario de colores
    colores = {"rojo": "red", "verde": "green", "negro": "black"}

    # Intentar acceder a una clave inexistente
    print(colores["blanco"])

except KeyError:
    print("Error: La clave especificada no existe en el diccionario. Verifique la clave antes de acceder.")

except Exception as e:  # Captura cualquier otro error inesperado
    print(f"Error inesperado: {e}")

finally:
    print("Operación finalizada.")
