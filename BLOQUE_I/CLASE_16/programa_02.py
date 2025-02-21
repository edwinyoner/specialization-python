"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este programa maneja el error IndexError cuando se intenta acceder a un índice
    que no existe en una lista.
"""

try:
    # Lista de ejemplo
    lista = [7, 4, 5]

    # Intentar acceder a un índice fuera de rango
    print(lista[10])

except IndexError:
    print("Error: El índice especificado no existe en la lista. Asegúrese de utilizar un índice válido.")

except Exception as e:  # Captura cualquier otro error inesperado
    print(f"Error inesperado: {e}")

finally:
    print("Operación finalizada.")
