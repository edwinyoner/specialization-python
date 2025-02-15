"""
Archivo: humano1.py
Autor: Edwin Yoner
Fecha: 13/02/2025

Descripción:
    Este módulo define una clase Humano con atributos de clase e instancia,
    así como métodos de instancia, de clase y estáticos.
"""


class Humano:
    """
    Clase que representa a un ser humano con nombre y una propiedad compartida de respiración.
    """

    # Atributo de clase (compartido por todas las instancias)
    respirar = True

    def __init__(self, nombre):
        """
        Constructor de la clase Humano.

        :param nombre: Nombre del humano (atributo de instancia).
        """
        self.nombre = nombre  # Atributo de instancia (único para cada objeto)

        # Llamado automático a métodos en la creación del objeto
        self.info()  # Método estático
        self.hablar()  # Método de instancia
        self.datos_generales()  # Método de clase

    def hablar(self):
        """
        Método de instancia que imprime un mensaje con el nombre del humano.
        """
        print(f"Hola, mi nombre es {self.nombre}")

    @classmethod
    def datos_generales(cls):
        """
        Método de clase que accede al atributo de clase.
        """
        print(f"Los seres humanos respiran: {cls.respirar}")

    @staticmethod
    def info():
        """
        Método estático que muestra un mensaje cuando se crea un objeto.
        """
        print("Se creó el objeto")


# Creación de la primera instancia de la clase Humano
juan = Humano("Juan")  # Se ejecutan los métodos automáticamente
juan.hablar()  # Llamada adicional al método hablar
print(f"¿Juan respira?: {juan.respirar}")

# Creación de la segunda instancia de la clase Humano
carlos = Humano("Carlos")  # Se ejecutan los métodos automáticamente
carlos.hablar()  # Llamada adicional al método hablar
print(f"¿Carlos respira?: {carlos.respirar}")

# Llamada al método de clase desde una instancia
carlos.datos_generales()

# Llamada al método estático desde la clase directamente
Humano.info()
