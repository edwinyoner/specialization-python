"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 06/02/2025

Descripción:
    Este programa demuestra el uso de anotaciones en funciones, parámetros con valores por defecto,
    asignación de funciones a variables y el uso de valores mutables en parámetros.
"""

# Anotaciones en funciones
def suma(x: int, y: int) -> int:
    """
    Retorna la suma de dos números enteros.
    """
    return x + y

resultado = suma(2, 3)
print("Suma con anotaciones:", resultado)  # Salida: 5

print("\n")

# Uso de valores por defecto con anotaciones
def suma(x: int = 0, y: int = 6) -> int:
    """
    Retorna la suma de dos números con valores por defecto.
    """
    return x + y

resultado = suma(2)
print("Suma con valor por defecto:", resultado)  # Salida: 8

print("\n")

# Asignación de una función a una variable
def suma(x, y):
    """
    Retorna la suma de dos valores.
    """
    return x + y

s = suma  # Asignación de la función a una nueva variable
suma = 10  # La variable 'suma' deja de ser una función y pasa a ser un entero

print("Suma utilizando variable asignada:", s(2, 4))  # Salida: 6

print("\n")

# Uso de valores mutables en parámetros (precaución con listas)
def apilar_lista(x, y=None):
    """
    Agrega un valor a una lista. Evita el uso de listas mutables como valores por defecto.
    """
    if y is None:
        y = []
    y.append(x)
    return y

# Verificando valores por defecto en la función
print("Valores por defecto:", apilar_lista.__defaults__)  # Salida: None

# Llamada a la función con diferentes valores
resultado = apilar_lista(2)
print("Lista después de apilar 2:", resultado)  # Salida: [2]

resultado = apilar_lista(3)
print("Lista después de apilar 3:", resultado)  # Salida: [3]

# Verificando nuevamente valores por defecto
print("Valores por defecto después de ejecución:", apilar_lista.__defaults__)  # Salida: None