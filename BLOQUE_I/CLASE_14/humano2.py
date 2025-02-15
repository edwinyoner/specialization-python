"""
Archivo: herencia.py
Autor: Edwin Yoner
Fecha: 13/02/2025

Descripción:
    Este módulo demuestra el concepto de herencia en la Programación Orientada a Objetos (POO),
    donde la clase Estudiante hereda de la clase Humano.
"""

class Humano:
    """
    Clase base que representa a un ser humano con un nombre.
    """

    def __init__(self, nombre: str):
        """
        Constructor de la clase Humano.

        :param nombre: Nombre del humano.
        """
        self.nombre = nombre

    def hablar(self):
        """
        Método de instancia que imprime un saludo con el nombre del humano.
        """
        print(f"Hola, soy {self.nombre}")


class Estudiante(Humano):  # Clase hija que hereda de Humano
    """
    Clase que representa a un estudiante, heredando las características de Humano.
    """

    def __init__(self, codigo: int, nombre: str):
        """
        Constructor de la clase Estudiante.

        :param codigo: Código único del estudiante.
        :param nombre: Nombre del estudiante.
        """
        super().__init__(nombre)  # Llamada al constructor de la clase base
        # Humano.__init__(self, nombre)
        self.codigo = codigo  # Nuevo atributo específico de Estudiante

    def presentarse(self):
        """
        Método de instancia que imprime un mensaje de presentación del estudiante,
        incluyendo su código y llamando al método hablar() heredado.
        """
        print(f"Hola, soy un estudiante con código {self.codigo}.")
        self.hablar()  # Llamada al método de la clase padre


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de una instancia de la clase Humano
    humano1 = Humano("Diego")
    humano1.hablar()  # Llamada al método hablar

    # Creación de una instancia de la clase Estudiante
    estudiante1 = Estudiante(1234, "Diego")

    # Uso de los métodos heredados y propios de la subclase
    estudiante1.hablar()  # Método heredado de Humano
    estudiante1.presentarse()  # Método propio de Estudiante
