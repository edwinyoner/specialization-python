"""
Archivo: operacion2.py
Autor: Edwin Yoner
Fecha: 11/02/2025

Descripción:
    Este módulo define una clase Operacion que permite realizar operaciones
    matemáticas básicas como suma y resta, utilizando dos números como atributos.
"""


class Operacion:
    """
    Clase que representa operaciones matemáticas básicas con dos números.
    """

    def __init__(self, num1, num2):
        """
        Constructor de la clase Operacion.

        :param num1: Primer número de la operación.
        :param num2: Segundo número de la operación.
        """
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        """
        Método para sumar los dos números.

        :return: Resultado de la suma.
        """
        return self.num1 + self.num2

    def restar(self):
        """
        Método para restar el segundo número del primero.

        :return: Resultado de la resta.
        """
        return self.num1 - self.num2


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de una instancia de la clase Operacion con valores 2 y 3
    op1 = Operacion(2, 3)

    # Impresión de los resultados de las operaciones
    print(f'La suma es = {op1.sumar()}')
    print(f'La resta es = {op1.restar()}')
