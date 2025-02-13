"""
Archivo: humano1.py
Autor: Edwin Yoner
Fecha: 11/02/2025

Descripción:
    Este módulo define una clase Humano con atributos nombre y edad,
    e incluye un método para hablar.
"""


class Humano:
    """
    Clase que representa a un ser humano con nombre y edad.
    """

    def __init__(self, nombre, edad):
        """
        Constructor de la clase Humano.

        :param nombre: Nombre del humano.
        :param edad: Edad del humano.
        """
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        """
        Método para imprimir un mensaje de presentación del humano.
        """
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años.')


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de una instancia de la clase Humano
    humano1 = Humano("Diego", 5)

    # Invocación del método hablar
    humano1.hablar()
