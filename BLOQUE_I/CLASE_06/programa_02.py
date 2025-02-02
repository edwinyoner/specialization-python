"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 25/01/2025

Descripción:
    Este programa demuestra el uso de las funciones de entrada y salida en Python,
    incluyendo `print()` y `input()`, junto con sus parámetros clave.
"""

# Mostrar la documentación de la función print()
help(print)

# Uso de print() con diferentes tipos de datos
x = 2
y = 4
z = "Hola"

print("\nEjemplo de print con parámetros:")
print(x, y, z, sep="-", end="     ")  # Separador personalizado y un final específico
print("AMIGO", 12, sep="@")  # Diferente separador entre elementos

# Mostrar la documentación de la función input()
help(input)

# Uso de input() para solicitar datos al usuario
x = input("\nIngrese un valor: ")  # Captura de entrada del usuario como string
print("El valor de x es:", x)  # Muestra el valor ingresado por el usuario
