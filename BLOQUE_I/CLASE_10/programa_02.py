"""
Archivo: cantidad_indeterminada.py
Autor: Edwin Yoner
Fecha: 04/02/2025

Descripción:
    Este programa muestra el uso de funciones en Python con parámetros de 
    cantidad indeterminada: por posición (*args), por nombre (**kwargs) 
    y combinaciones de ambos.
"""

# Parámetros por posición ( *args )
def suma(*args):
    """
    Retorna los valores pasados como argumentos en forma de tupla.
    """
    return args

print("Suma por posición:", suma(1, 2, 3, 4))

print("\n")

# Sumar n números usando *args
def suma_de_numeros(*args):
    """
    Retorna la suma de todos los valores pasados como argumentos.
    """
    return sum(args)

print("Suma de los n números es:", suma_de_numeros(1, 2, 3, 4, 5))

print("\n")

# Calcular el factorial de un número
def factorial(valor):
    """
    Calcula el factorial de un número dado.
    """
    fact = 1
    for i in range(1, valor + 1):
        fact *= i
    return fact

print(f"El factorial de 5 es: {factorial(5)}")

print("\n")

# Parámetros por nombre ( **kwargs )
def suma(**kwargs):
    """
    Retorna los valores pasados como argumentos con nombre en forma de diccionario.
    """
    return kwargs

print("Suma por nombre:", suma(a=1, b=2, c=3, d=4))

print("\n")

# Sumar valores usando **kwargs
def suma(**kwargs):
    """
    Retorna la suma de los valores en el diccionario de argumentos con nombre.
    """
    return sum(kwargs.values())

print("La suma es:", suma(a=1, b=2, c=3, d=4))

print("\n")

# Iterar sobre un diccionario
a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Iteración sobre un diccionario:")
for clave, valor in a.items():
    print(f"{clave}: {valor}")

print("\n")

# Combinación de *args y **kwargs
def suma(*args, **kwargs):
    """
    Retorna la suma de los valores en *args y **kwargs.
    """
    total_args = sum(args)
    total_kwargs = sum(kwargs.values())
    return total_args + total_kwargs

print("La suma total es:", suma(3, 4, 3, a=1, b=2, c=3, d=4))

print("\n")

# Combinación con parámetros por defecto
def suma(x, y, *args, w=0, z=1, **kwargs):
    """
    Retorna la suma de los valores x, y y z, ignorando otros argumentos.
    """
    return x + y + z

print("Suma combinada 1:", suma(1, 2, 3, 4, 6))
print("Suma combinada 2:", suma(1, 2, 3, z=2))
print("Suma combinada 3:", suma(1, 2, 3, a=2, b=3))

print("\n")

# Retornar solo los valores **kwargs
def suma(*args, w=0, z=1, **kwargs):
    """
    Retorna el diccionario de argumentos con nombre.
    """
    return kwargs

print("Solo kwargs 1:", suma(1, 2, 3, 4, 6))
print("Solo kwargs 2:", suma(1, 2, 3, z=2))
print("Solo kwargs 3:", suma(1, 2, 3, a=2))