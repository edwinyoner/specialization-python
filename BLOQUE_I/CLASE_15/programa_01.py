"""
Archivo: programa_01py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este módulo demuestra diferentes formas de calcular el cuadrado de cada número en una lista,
    utilizando funciones tradicionales, `map` con funciones definidas y `lambda`,
    así como listas por comprensión para una solución más eficiente.
"""

# Lista de números originales
numeros = [1, 2, 3, 4, 5]


# 1. Función tradicional con listas por comprensión
def calcular_cuadrados(lista_numeros):
    """
    Recibe una lista de números y devuelve una nueva lista con los valores elevados al cuadrado.

    :param lista_numeros: Lista de números enteros.
    :return: Nueva lista con los cuadrados de los números originales.
    """
    return [numero ** 2 for numero in lista_numeros]  # Utilizando listas por comprensión


# Imprimir el resultado usando la función tradicional
print("1. Usando función tradicional:", calcular_cuadrados(numeros))


# 2. Usando `map` con función definida
def calcular_cuadrado(numero):
    """
    Calcula el cuadrado de un número.

    :param numero: Número entero.
    :return: Cuadrado del número.
    """
    return numero ** 2


# Aplicando `map` con una función definida
resultado_map = list(map(calcular_cuadrado, numeros))
print("2. Usando map con función definida:", resultado_map)

# 3. Usando `map` con función lambda
resultado_lambda = list(map(lambda numero: numero ** 2, numeros))
print("3. Usando map con función lambda:", resultado_lambda)

# 4. Usando listas por comprensión directamente
resultado_comprension = [numero ** 2 for numero in numeros]
print("4. Usando listas por comprensión:", resultado_comprension)


