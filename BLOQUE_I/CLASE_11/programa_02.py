"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 06/02/2025

Descripción:
    Este programa demuestra el uso de la recursividad en Python a través de
    diferentes ejemplos como impresión de mensajes en orden y reverso,
    además del cálculo del factorial de un número.
"""

# Ejemplo 1: Imprimir una secuencia en orden descendente
def mensaje_descendente(x):
    """
    Imprime los números de x a 1 de manera descendente.
    """
    if x > 0:
        print(x)
        mensaje_descendente(x - 1)

print("Mensaje descendente:")
mensaje_descendente(4)  # Salida: 4, 3, 2, 1

print("\n")

# Ejemplo 2: Imprimir una secuencia en orden ascendente
def mensaje_ascendente(x):
    """
    Imprime los números de 1 a x de manera ascendente.
    """
    if x > 0:
        mensaje_ascendente(x - 1)
        print(x)

print("Mensaje ascendente:")
mensaje_ascendente(4)  # Salida: 1, 2, 3, 4

print("\n")

# Ejemplo 3: Manejo del caso base en recursión
def mensaje(x):
    """
    Imprime números de 1 a x asegurando un caso base para evitar recursión infinita.
    """
    if x <= 0:  # Caso Base
        return
    else:
        mensaje(x - 1)
        print(x)

print("Mensaje con caso base:")
mensaje(5)  # Salida: 1, 2, 3, 4, 5

print("\n")

# Ejemplo 4: Factorial usando recursividad
def factorial(n):
    """
    Retorna el factorial de un número n usando recursión.
    """
    if n == 0:
        return 1  # Caso Base
    else:
        return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))  # Salida: 120