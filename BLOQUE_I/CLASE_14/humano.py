"""
Archivo: humano.py
Autor: Edwin Yoner
Fecha: 13/02/2025

Descripción:
    Este módulo define una clase Humano con atributos de clase e instancia,
    y métodos para interactuar con ellos.
"""


class Humano:
    """
    Clase que representa a un ser humano con un nombre y una lista compartida
    para la acción de respirar.
    """

    # Atributo de clase (compartido por todas las instancias)
    respirar = []

    def __init__(self, nombre):
        """
        Constructor de la clase Humano.

        :param nombre: Nombre del humano (atributo de instancia).
        """
        self.nombre = nombre  # Atributo de instancia (único para cada objeto)

    def hablar(self):
        """
        Método de instancia que imprime un mensaje con el nombre del humano.
        """
        print(f"Hola, mi nombre es {self.nombre}")


# Creación de la primera instancia de la clase Humano
juan = Humano("Juan")
juan.hablar()  # Llamada al método hablar

# Modificación del atributo de clase a través de la instancia
juan.respirar.append(2)
print(f"Atributo de clase 'respirar' desde Juan: {juan.respirar}")

# Creación de una segunda instancia de la clase Humano
carlos = Humano("Carlos")
carlos.hablar()  # Llamada al método hablar

# Verificación de que el atributo de clase es compartido entre instancias
print(f"Atributo de clase 'respirar' desde Carlos: {carlos.respirar}")
