"""
Archivo: modulo1.py
Autor: Edwin Yoner
Fecha: 08/02/2025

Descripción:
    Este módulo contiene una función `suma` para realizar una operación matemática básica.
    Además, incluye una verificación de ejecución directa con `__name__ == "__main__"`.
"""


# Definición de la función `suma`
def suma(x, y):
    """
    Retorna la suma de dos números.

    Parámetros:
    x (int, float): Primer número
    y (int, float): Segundo número

    Retorna:
    int, float: Resultado de la suma
    """
    return x + y


# Código de prueba cuando el módulo se ejecuta directamente
if __name__ == "__main__":
    print("Hola :)")  # Se ejecuta solo si este archivo se ejecuta directamente
    # print(__name__)  # Muestra el nombre del módulo
