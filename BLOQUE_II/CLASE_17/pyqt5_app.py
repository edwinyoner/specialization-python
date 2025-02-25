"""
Archivo: pyqt5_app.py
Autor: Edwin Yoner
Fecha: 18/02/2025

Descripción:
    Este programa crea una interfaz gráfica con PyQt5 que incluye un label,
    dos botones ("Activar" y "Desactivar") y un slider. Se manejan eventos
    para detectar clics en los botones y cambios en el slider.
"""

import os

# Configuración de la variable de entorno para PyQt5
os.environ[
    "QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

# Importamos los módulos de PyQt5 necesarios
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QSlider
from PyQt5.QtCore import Qt


class App(QWidget):
    """
    Clase que representa la ventana principal de la aplicación PyQt5.
    """

    def __init__(self):
        """
        Constructor de la clase App. Configura la interfaz y la inicializa.
        """
        super().__init__()

        # Definimos propiedades de la ventana
        self.ancho = 600
        self.alto = 300
        self.pos_x = 100
        self.pos_y = 100
        self.titulo = "PROYECTO PyQt5"

        # Inicialización de la interfaz
        self.initUI()

    def initUI(self):
        """
        Método que configura los elementos gráficos de la ventana.
        """
        # Configuración de la ventana
        self.setGeometry(self.pos_x, self.pos_y, self.ancho, self.alto)
        self.setWindowTitle(self.titulo)

        # Crear un label (etiqueta de texto)
        self.label = QLabel("PROTOTIPO - I", self)
        self.label.move(230, 100)
        self.label.setStyleSheet("font-size: 20px; color: orange")

        # Crear botón ACTIVAR
        self.boton_activar = QPushButton("ACTIVAR", self)
        self.boton_activar.move(180, 150)
        self.boton_activar.clicked.connect(self.activar)

        # Crear botón DESACTIVAR
        self.boton_desactivar = QPushButton("DESACTIVAR", self)
        self.boton_desactivar.move(300, 150)
        self.boton_desactivar.clicked.connect(self.desactivar)

        # Crear un slider (barra deslizante)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(230, 200, 200, 30)
        self.slider.valueChanged.connect(self.mostrar_datos)

        # Mostrar la ventana
        self.show()

    def activar(self):
        """
        Método que se ejecuta cuando se presiona el botón "ACTIVAR".
        """
        print("Activado")

    def desactivar(self):
        """
        Método que se ejecuta cuando se presiona el botón "DESACTIVAR".
        """
        print("Desactivado")

    def mostrar_datos(self, valor):
        """
        Método que se ejecuta cuando cambia el valor del slider.

        :param valor: Valor actual del slider.
        """
        print(f"Valor del slider: {valor}")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    # Crear la aplicación
    app = QApplication([])

    # Crear y mostrar la ventana
    ventana = App()

    # Ejecutar la aplicación
    app.exec_()