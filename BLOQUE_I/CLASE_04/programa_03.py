"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 21/01/2025

Descripción:
    Este programa muestra cómo manipular strings en Python, 
    incluyendo asignación de valores, indexación y slicing.
"""

# Asignación de valores a variables tipo string
m = "hola"  # Asignamos un string a la variable m
m = "a"  # Sobreescribimos el valor de m
a = "2"  # Almacenamos un número como string en la variable a

# Indexación en Strings
# Se puede acceder a un carácter específico usando su índice
nombre = "juan perez"
print(f"Segundo carácter del string: {nombre[1]}")  # Salida: 'u'

# Slicing en Strings
# Permite extraer una subcadena desde una posición específica hasta el final
print(f"Subcadena desde la posición 5: {nombre[5:]}")  # Salida: 'perez'
