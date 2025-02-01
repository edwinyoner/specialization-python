"""
Archivo: programa_04.py
Autor: Edwin Yoner
Fecha: 21/01/2025

Descripción:
    Este programa muestra el uso de diferentes métodos de strings en Python,
    incluyendo capitalize(), count() y lower().
"""

# Método capitalize(): Convierte la primera letra del string en mayúscula
x = "juan"
print("Antes de capitalize():", x)
x = x.capitalize()
print("Después de capitalize():", x)

# Método count(): Cuenta cuántas veces aparece una subcadena en un string
x = "los osos perezosos"
cantidad = x.count("oso")
print(f"Número de ocurrencias de 'oso': {cantidad}")  # Salida: 2

# Método lower(): Convierte todo el string a minúsculas
x = "JUAN"
x = x.lower()
print("Después de lower():", x)
