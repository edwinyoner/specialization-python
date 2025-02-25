"""
Archivo: temporizador_pyqt5.py
Autor: Edwin Yoner
Fecha: 20/02/2025

Descripción:
    Este programa crea una interfaz gráfica con PyQt5 que muestra un QLabel (etiqueta)
    y un QTimer (temporizador). El temporizador incrementa un contador y actualiza
    el texto de la etiqueta cada segundo.

Requisitos:
    - Tener instalada la librería PyQt5.

Componentes de la interfaz:
    - Una ventana principal con un título personalizado.
    - Un QLabel que inicialmente muestra "Esperando...".
    - Un QTimer que actualiza la etiqueta cada segundo con un contador.
"""

import os

# Configuración de la variable de entorno para PyQt5 en macOS
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

# Importamos los módulos necesarios de PyQt5
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer

class App(QWidget):
    """
    Clase principal de la aplicación PyQt5 que hereda de QWidget.
    """

    def __init__(self):
        """
        Constructor de la clase App. Define las propiedades de la ventana principal y la inicializa.
        """
        super().__init__()

        # Definimos las dimensiones y posición de la ventana
        self.w = 500  # Ancho de la ventana
        self.h = 250  # Alto de la ventana
        self.x = 100  # Posición X de la ventana
        self.y = 100  # Posición Y de la ventana
        self.titulo = "PROYECTO"  # Título de la ventana

        # Llamamos al método para inicializar la interfaz gráfica
        self.initUI()

    def initUI(self):
        """
        Método que configura los elementos de la interfaz gráfica.
        """
        # Configuramos la geometría de la ventana (posición y tamaño)
        self.setGeometry(self.x, self.y, self.w, self.h)

        # Establecemos el título de la ventana
        self.setWindowTitle(self.titulo)

        # Creamos un QLabel (Etiqueta) que muestra un mensaje inicial
        self.label = QLabel("Esperando...", self)
        self.label.setGeometry(100, 80, 150, 30)  # Establecemos la posición y tamaño

        # Creamos un QTimer (Temporizador)
        timer = QTimer(self)  # Inicializamos el temporizador
        timer.timeout.connect(self.mostrar_mensaje)  # Conectamos el temporizador al método
        timer.start(1000)  # Configuramos el temporizador para que se ejecute cada 1000ms (1 segundo)

        # Inicializamos el contador en 0
        self.contador = 0

        # Mostramos la ventana con todos los elementos
        self.show()

    def mostrar_mensaje(self):
        """
        Método que se ejecuta cada vez que el temporizador llega al timeout.
        - Incrementa el contador en 1.
        - Imprime el valor del contador en la consola.
        - Actualiza el texto de la etiqueta con el nuevo valor del contador.
        """
        self.contador += 1
        print("Hola:", self.contador)  # Imprime el contador en la consola
        self.label.setText(str(self.contador))  # Actualiza el QLabel con el nuevo valor

# Bloque principal de ejecución
if __name__ == "__main__":
    # Creamos la aplicación Qt
    app = QApplication([])

    # Creamos una instancia de la clase App (nuestra interfaz gráfica)
    ex = App()

    # Ejecutamos el bucle de eventos de la aplicación
    app.exec_()
