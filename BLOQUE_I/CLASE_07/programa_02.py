"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 28/01/2025

Descripción:
    Este programa solicita una nota al usuario y determina si ha aprobado
    o no, utilizando una estructura condicional simple.
"""

# Solicitar la nota al usuario
nota = float(input("Ingrese su nota: "))

# Evaluar si la nota es suficiente para aprobar
if nota >= 11:
    print("¡Felicidades! Has aprobado.")
else:
    print("Lo siento, has desaprobado. ¡Sigue esforzándote!")