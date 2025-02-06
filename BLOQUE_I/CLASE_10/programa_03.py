"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 04/02/2025

Descripción:
    Este programa demuestra el uso de funciones en Python para realizar sumas.
    Se incluyen ejemplos de funciones que retornan valores y funciones que imprimen
    directamente el resultado. Además, se muestra cómo manejar el retorno de valores
    y la impresión en diferentes contextos.
"""

# Función que retorna la suma de dos números
def suma(x, y):
    """
    Retorna la suma de dos números pasados como parámetros.

    Parámetros:
    x (int o float): Primer número a sumar.
    y (int o float): Segundo número a sumar.

    Retorna:
    int o float: La suma de x e y.
    """
    c = x + y
    return c

# Llamada a la función y almacenamiento del resultado en la variable 'r'
r = suma(2, 3)
print("Resultado de la suma (retorno):", r)  # Salida: 5

# Función que imprime la suma de dos números directamente
def suma(x, y):
    """
    Imprime la suma de dos números pasados como parámetros.

    Parámetros:
    x (int o float): Primer número a sumar.
    y (int o float): Segundo número a sumar.
    """
    c = x + y
    print("Resultado de la suma (impresión directa):", c)

# Llamada a la función que imprime directamente el resultado
r = suma(2, 3)  # Esta función no retorna ningún valor, por lo que 'r' será None
print("Retorno de la función que imprime directamente:", r)  # Salida: None