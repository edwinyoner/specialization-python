"""
Archivo: humano2.py
Autor: Edwin Yoner
Fecha: 11/02/2025

Descripción:
    Este módulo define una clase Humano con atributos nombre y edad,
    e incluye métodos para inicializar los atributos y para hablar.
"""


class Humano:
    """
    Clase que representa a un ser humano con nombre y edad.
    """

    def init(self, nombre, edad):
        """
        Método para asignar valores a los atributos nombre y edad.

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
    # Creación de una instancia de la clase Humano sin valores iniciales
    humano1 = Humano()

    # Uso del método init para asignar valores a los atributos
    humano1.init("Juan", 30)

    # Invocación del método hablar
    humano1.hablar()
