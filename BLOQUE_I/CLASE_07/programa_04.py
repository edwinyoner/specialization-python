"""
Archivo: programa_04.py
Autor: Edwin Yoner
Fecha: 28/01/2025

Descripción:
    Este programa solicita un número al usuario y determina si es par o impar 
    utilizando estructuras condicionales.
"""

# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Primera forma con dos condiciones separadas
if numero % 2 == 0:
    print("Número par")
if numero % 2 != 0:
    print("Número impar")

# Segunda forma optimizada con if-else
if numero % 2 == 0:
    print("Número par")
else:
    print("Número impar")

# Alternativa con operador ternario
print("Número par" if numero % 2 == 0 else "Número impar")