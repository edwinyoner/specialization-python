"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 23/01/2025

Descripción:
    Este programa demuestra la creación y uso de clases en Python. 
    Se define una clase `Humano` con atributos y métodos, además de 
    explorar los tipos de los objetos instanciados.
"""

# Definición de la clase Humano
class Humano:
    """
    Clase que representa a un humano con nombre y edad.

    Atributos:
    nombre (str): Nombre del humano.
    edad (int): Edad del humano.

    Métodos:
    hablar(): Muestra un mensaje indicando que el objeto puede hablar.
    """
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Humano.

        Parámetros:
        nombre (str): Nombre de la persona.
        edad (int): Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        """
        Método que imprime un mensaje indicando que el objeto puede hablar.
        """
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creación de un objeto de la clase Humano
humano1 = Humano("Edwin", 10)

# Mostrar el tipo de la instancia y la clase
print(f"Tipo del objeto 'humano1': {type(humano1)}")  # <class '__main__.Humano'>
print(f"Tipo de la clase 'Humano': {type(Humano)}")  # <class 'type'>

# Llamada al método hablar
humano1.hablar()
