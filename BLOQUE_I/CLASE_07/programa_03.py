"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 28/01/2025

Descripción:
    Este programa solicita la edad de un usuario y determina si es mayor
    o menor de edad utilizando estructuras condicionales.
"""

# Solicitar la edad al usuario
edad = int(input("Ingrese su edad: "))

# Evaluar la mayoría de edad con condicionales
if edad >= 18:
    print("Mayor de Edad")
else:
    print("Menor de Edad")

# Alternativa con operador ternario
print("Mayor de Edad" if edad >= 18 else "Menor de Edad")


