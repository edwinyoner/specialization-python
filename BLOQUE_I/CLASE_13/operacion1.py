"""
Archivo: operacion.py
Autor: Edwin Yoner
Fecha: 11/02/2025

Descripción:
    Este módulo define una clase Operacion con métodos para sumar y restar dos números.
"""


class Operacion:
    """
    Clase que representa operaciones matemáticas básicas.
    """

    def sumar(self, num1, num2):
        """
        Método para sumar dos números.

        :param num1: Primer número.
        :param num2: Segundo número.
        :return: Resultado de la suma.
        """
        return num1 + num2

    def restar(self, num1, num2):
        """
        Método para restar dos números.

        :param num1: Primer número.
        :param num2: Segundo número.
        :return: Resultado de la resta.
        """
        return num1 - num2


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de una instancia de la clase Operacion
    op1 = Operacion()

    # Definición de los números a operar
    num1 = 5
    num2 = 3

    # Uso de los métodos de la clase Operacion
    print(f'La suma de {num1} + {num2} es = {op1.sumar(num1, num2)}')
    print(f'La resta de {num1} - {num2} es = {op1.restar(num1, num2)}')
