"""
2**3 = 2 * 2**2 = 2 * 2 * 2**1 = 2 * 2 * 2**0
potencia(2, 3) = 2 * potencia(2, 2) caso recursivo return base * potencia(base, exponente - 1)
potencia(2, 2) = 2 * potencia(2, 1)
potencia(2, 1) = 2 * potencia(2, 0)
potencia(2, 0) = 1 -> caso base return 1
potencia(0, n) = 0 -> caso base return 0
"""
def potencia(base, exponente):
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
Se tiene la siguiente lista s = [2, 3, 4, 1, 0, 5], añadir al modulo anterior
una función que sume los elementos de la lista de manera recursiva
"""

def suma_recursiva_lista(lista, i=0):
    if i >= len(lista):  # Caso base
        return 0
    return lista[i] + suma_recursiva_lista(lista, i + 1)  # Caso recursivo


s = [2, 3, 4, 1, 0, 5]

print("Suma de la lista:", suma_recursiva_lista(s))

"""
Llamada	                    i	    lista[i]	Expresión evaluada
suma_recursiva_lista(s )	0	=   2	        2 + suma_recursiva_lista(s, 1)
suma_recursiva_lista(s, 1)	1	=   3	        3 + suma_recursiva_lista(s, 2)
suma_recursiva_lista(s, 2)	2	=   4	        4 + suma_recursiva_lista(s, 3)
suma_recursiva_lista(s, 3)	3	=   1	        1 + suma_recursiva_lista(s, 4)
suma_recursiva_lista(s, 4)	4	=   0	        0 + suma_recursiva_lista(s, 5)
suma_recursiva_lista(s, 5)	5	=   5	        5 + suma_recursiva_lista(s, 6)
suma_recursiva_lista(s, 6)	6	    x           (fuera de rango) Retorna 0
"""


"""
suma_recursiva_lista(s, 6) → retorna 0
suma_recursiva_lista(s, 5) → 5 + 0 = 5
suma_recursiva_lista(s, 4) → 0 + 5 = 5
suma_recursiva_lista(s, 3) → 1 + 5 = 6
suma_recursiva_lista(s, 2) → 4 + 6 = 10
suma_recursiva_lista(s, 1) → 3 + 10 = 13
suma_recursiva_lista(s, 0) → 2 + 13 = 15
"""