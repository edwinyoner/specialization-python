"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 23/01/2025

Descripción:
    Este programa demuestra la definición y uso de funciones en Python, 
    incluyendo la obtención de información sobre las funciones con `type()` y `help()`.
"""

# Definición de una función que suma dos números
def suma(x, y):
    """
    Función que recibe dos números y retorna su suma.

    Parámetros:
    x (int, float): Primer número.
    y (int, float): Segundo número.

    Retorna:
    int, float: Resultado de la suma de x e y.
    """
    return x + y  # Retorna la suma de los parámetros

# Obtener información sobre la función
print(f"El tipo de dato de 'suma' es: {type(suma)}")

# Mostrar documentación de la función
help(suma)

# Mostrar información sobre el tipo 'function'
help(type(suma))

# Llamar a la función y mostrar el resultado
resultado = suma(2, 3)
print(f"Resultado de suma(2, 3): {resultado}")  # Salida esperada: 5
