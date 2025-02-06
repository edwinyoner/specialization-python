"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 04/02/2025

Descripción:
    Este programa demuestra el uso de funciones en Python con diferentes tipos de
    parámetros en una cantidad determinada: por posición, por nombre, con valores
    por defecto y combinación de parámetros.
"""

# Parámetros por posición u orden
def suma(x, y):
    """
    Retorna la suma de dos números pasados por posición.
    """
    return x + y

print("Suma por posición:", suma(2, 3))  # Salida: 5

print("\n")

# Parámetros por nombre
def suma(x, y):
    """
    Retorna la suma de dos números pasados por nombre.
    """
    print(f"x: {x}, y: {y}")
    return x + y

print("Suma por nombre:", suma(y=2, x=3))  # Salida: 5

print("\n")

# Parámetros con valores por defecto
def suma(x=0, y=0):
    """
    Retorna la suma de dos números, permitiendo valores por defecto.
    """
    print(f"x: {x}, y: {y}")
    return x + y

print("Suma con valores por defecto:", suma(y=4))  # Salida: 4

print("\n")

# Combinación de parámetros
def suma(x, y, z=0, w=5):
    """
    Retorna el resultado de la operación (x + y - z - w).
    """
    return x + y - z - w

# Diferentes formas de llamar a la función combinada
print("Suma combinada 1:", suma(2, 3))  # Salida: 0 (2 + 3 - 0 - 5)
print("Suma combinada 2:", suma(1, 2, 6, 8))  # Salida: -11 (1 + 2 - 6 - 8)
print("Suma combinada 3:", suma(1, 2, w=0))  # Salida: 3 (1 + 2 - 0 - 0)
print("Suma combinada 4:", suma(x=1, y=2, w=6))  # Salida: -3 (1 + 2 - 0 - 6)