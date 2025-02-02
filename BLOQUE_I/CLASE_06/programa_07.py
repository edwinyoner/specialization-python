"""
Archivo: programa.py
Autor: Edwin Yoner
Fecha: 25/01/2025

Descripción:
    Este programa solicita una nota al usuario y determina si el estudiante
    ha "Aprobado" o "Desaprobado" utilizando una lista y una condición booleana.
"""

# Solicitar la nota al usuario
nota = int(input("Ingrese su nota: "))

# Lista con los posibles resultados
resultado = ["Desaprobado", "Aprobado"]

# Determinar el estado de aprobación usando una condición booleana
estado = resultado[nota >= 12]

# Mostrar el resultado
print(f"El estudiante está {estado}.")