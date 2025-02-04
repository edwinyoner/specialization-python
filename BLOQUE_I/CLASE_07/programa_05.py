"""
Archivo: programa_05.py
Autor: Edwin Yoner
Fecha: 28/01/2025

Descripción:
    Este programa solicita dos notas al usuario, calcula el promedio y
    determina si el estudiante aprueba o desaprueba según su calificación.
"""

# Solicitar las notas al usuario
nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))

# Cálculo del promedio
promedio = (nota1 + nota2) / 2

# Determinar si el estudiante aprueba o desaprueba
if promedio >= 11:
    mensaje = f"Aprobado con promedio: {promedio}"
else:
    mensaje = f"Desaprobado con promedio: {promedio}"

# Imprimir el resultado
print(mensaje)