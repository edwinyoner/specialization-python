"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este módulo demuestra diferentes formas de filtrar números múltiplos de 5 en una lista,
    utilizando la función `filter` con una función definida y una función lambda,
    así como listas por comprensión para una solución más eficiente.
"""

# Lista de números originales
numeros = [2, 5, 10, 23, 50, 33]

# 1. Usando la función filter con una función definida
def es_multiplo_de_cinco(numero):
    """
    Verifica si un número es múltiplo de 5.

    :param numero: Número entero a evaluar.
    :return: True si el número es múltiplo de 5, False en caso contrario.
    """
    return numero % 5 == 0

# Aplicar filter con la función definida
resultado_filter_funcion = list(filter(es_multiplo_de_cinco, numeros))
print("1. Usando filter con función definida:", resultado_filter_funcion)

# 2. Usando la función filter con una función lambda
resultado_filter_lambda = list(filter(lambda numero: numero % 5 == 0, numeros))
print("2. Usando filter con función lambda:", resultado_filter_lambda)

# 3. Usando listas por comprensión
resultado_comprension = [numero for numero in numeros if numero % 5 == 0]
print("3. Usando listas por comprensión:", resultado_comprension)
