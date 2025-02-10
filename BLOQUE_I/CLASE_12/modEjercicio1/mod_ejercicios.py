"""
Archivo: mod_ejercicios.py
Autor: Edwin Yoner
Fecha: 08/02/2025

Descripción:
    Este módulo contiene funciones recursivas para calcular la potencia de un número
    y para sumar los elementos de una lista.
"""

def potencia(base, exponente):
    """
    Calcula la potencia de un número de forma recursiva.

    Parámetros:
    base (int, float): Base de la potencia.
    exponente (int): Exponente al que se eleva la base.

    Retorna:
    int, float: Resultado de base elevado a la potencia exponente.

    Casos Base:
    - Si el exponente es 0, retorna 1 (caso base de cualquier número elevado a 0).
    - Si la base es 0 y el exponente es mayor que 0, retorna 0 (optimización).
    """
    # Caso base: exponente es 0
    if exponente == 0:
        return 1
    # Caso base: base es 0 (evita cálculos innecesarios)
    elif base == 0:
        return 0
    # Paso recursivo
    else:
        return base * potencia(base, exponente - 1)
"""
Análisis
2**3 = 2 * 2**2 = 2 * 2 * 2**1 = 2 * 2 * 2**0
potencia(2, 3) = 2 * potencia(2, 2) caso recursivo return base * potencia(base, exponente - 1)
potencia(2, 2) = 2 * potencia(2, 1)
potencia(2, 1) = 2 * potencia(2, 0)
potencia(2, 0) = 1 -> caso base return 1
potencia(0, n) = 0 -> caso base return 0
"""

def suma_recursiva_lista(lista, i=0):
    """
    Suma los elementos de una lista de manera recursiva.

    Parámetros:
    lista (list): Lista de números.
    i (int): Índice actual de la lista. Predeterminado en 0.

    Retorna:
    int: La suma de todos los elementos de la lista.

    Casos Base:
    - Si el índice `i` es mayor o igual a la longitud de la lista, retorna 0.
    """
    if i >= len(lista):  # Caso base: si el índice supera el tamaño de la lista, retorna 0
        return 0
    return lista[i] + suma_recursiva_lista(lista, i + 1)  # Caso recursivo

"""
Análisis
Llamada	                    i	    lista[i]	Expresión evaluada
suma_recursiva_lista(s )	0	=   2	        2 + suma_recursiva_lista(s, 1)
suma_recursiva_lista(s, 1)	1	=   3	        3 + suma_recursiva_lista(s, 2)
suma_recursiva_lista(s, 2)	2	=   4	        4 + suma_recursiva_lista(s, 3)
suma_recursiva_lista(s, 3)	3	=   1	        1 + suma_recursiva_lista(s, 4)
suma_recursiva_lista(s, 4)	4	=   0	        0 + suma_recursiva_lista(s, 5)
suma_recursiva_lista(s, 5)	5	=   5	        5 + suma_recursiva_lista(s, 6)
suma_recursiva_lista(s, 6)	6	    x           (fuera de rango) Retorna 0

suma_recursiva_lista(s, 6) → retorna 0
suma_recursiva_lista(s, 5) → 5 + 0 = 5
suma_recursiva_lista(s, 4) → 0 + 5 = 5
suma_recursiva_lista(s, 3) → 1 + 5 = 6
suma_recursiva_lista(s, 2) → 4 + 6 = 10
suma_recursiva_lista(s, 1) → 3 + 10 = 13
suma_recursiva_lista(s, 0) → 2 + 13 = 15
"""