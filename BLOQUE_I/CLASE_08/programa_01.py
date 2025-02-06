"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 30/01/2025

Descripción:
    Este programa muestra el uso de la estructura repetitiva `for` en Python.
    Se presentan ejemplos de iteración sobre tuplas, diccionarios y rangos.
"""

# Iterar sobre una tupla e imprimir cada elemento
tupla = (2, 3, 4, 1, 3)
print("Elementos de la tupla:")
for elemento in tupla:
    print(elemento)

print("\n")

# Iterar sobre un diccionario e imprimir clave y valor
frutas_colores = {"manzana": "rojo", "pera": "verde"}
print("Colores de las frutas:")
for fruta, color in frutas_colores.items():
    print(f"{fruta}: {color}")

print("\n")

# Usar range() para repetir un mensaje 10 veces
print("Impresión de 'Hola' 10 veces:")
for _ in range(10):
    print("Hola")

print("\n")

# Usar range() con paso personalizado
print("Impresión con valores en rango:")
for i in range(2, 10, 2):
    print(f"Hola {i}")