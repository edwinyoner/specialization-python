"""
Archivo: humano.py
Autor: Edwin Yoner
Fecha: 11/02/2025

Descripción:
    Este módulo define una clase Humano con métodos para hablar y saludar.
"""


class Humano:
    """
    Clase que representa a un ser humano con la capacidad de hablar y saludar.
    """

    def __init__(self):
        """
        Constructor de la clase Humano.
        Inicializa el atributo mensaje con una cadena vacía.
        """
        self.mensaje = ""

    def hablar(self, mensaje):
        """
        Método para asignar un mensaje al atributo mensaje y mostrarlo en pantalla.

        :param mensaje: Texto que el objeto humano dirá.
        """
        self.mensaje = mensaje
        print(self.mensaje)

    def saludar(self):
        """
        Método para imprimir el mensaje almacenado previamente.
        """
        print(self.mensaje)


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de una instancia de la clase Humano
    humano1 = Humano()

    # Invocación del método hablar
    humano1.hablar("Hola")

    # Invocación del método saludar
    humano1.saludar()

    # Acceso al atributo mensaje
    print(f"Mensaje almacenado: {humano1.mensaje}")

    # Verificación de tipos de las instancias y la clase
    print(f"Tipo de humano1: {type(humano1)}")
    print(f"Tipo de la clase Humano: {type(Humano)}")
