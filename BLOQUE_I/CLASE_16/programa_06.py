"""
Archivo: programa_06.py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este programa define una función `suma` y utiliza `assert` para verificar 
    que el resultado no sea negativo. Se implementa manejo de excepciones para 
    capturar posibles errores.
"""

def suma(x, y):
    """
    Retorna la suma de dos números.

    :param x: Primer número (int o float).
    :param y: Segundo número (int o float).
    :return: Resultado de la suma.
    """
    return x + y

try:
    # Prueba de la función suma
    resultado = suma(3, 4)

    # Verificación con assert
    assert resultado >= 0, f"Error: La suma retornó un valor negativo ({resultado})"

    print(f"Resultado de la suma: {resultado}")

except AssertionError as e:
    print(e)

except Exception as e:
    print(f"Error inesperado: {e}")
