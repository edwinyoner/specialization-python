"""
Archivo: operacion3.py
Autor: Edwin Yoner
Fecha: 11/02/2025

Descripción:
    Este módulo define una clase Operacion que permite realizar operaciones
    matemáticas básicas como suma y resta, soportando parámetros opcionales.
"""


class Operacion:
    """
    Clase que representa operaciones matemáticas básicas con dos números base.
    """

    def __init__(self, num1: int = 0, num2: int = 0) -> None:
        """
        Constructor de la clase Operacion.

        :param num1: Primer número de la operación, valor por defecto 0.
        :param num2: Segundo número de la operación, valor por defecto 0.
        """
        self.num1 = num1
        self.num2 = num2

    def sumar(self, *args: int) -> int:
        """
        Método para calcular la suma de múltiples números incluyendo los atributos base.

        :param args: Números adicionales a sumar.
        :return: Resultado de la suma.
        """
        return sum(args) + self.num1 + self.num2

    def restar(self) -> int:
        """
        Método para calcular la resta entre los dos números base.

        :return: Resultado de la resta (num1 - num2).
        """
        return self.num1 - self.num2


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de una instancia de la clase Operacion con valores 2 y 3
    op1 = Operacion(2, 3)

    # Impresión de los resultados de las operaciones
    print(f'La suma es = {op1.sumar()}')  # Suma de los valores iniciales (2 + 3)
    print(f'La resta es = {op1.restar()}')  # Resta de los valores iniciales (2 - 3)

    # Uso de la función help() para documentación
    help(Operacion)
    help(op1)
    help(op1.sumar)
