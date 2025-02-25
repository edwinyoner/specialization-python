"""
Archivo: ventana.py
Autor: Edwin Yoner
Fecha: 18/02/2025

Descripción:
    Este programa crea una interfaz gráfica básica utilizando PyQt5.
    Contiene un QLabel (etiqueta), un QPushButton (botón) y un QSlider (deslizador).
    Se maneja la interacción con el botón y el slider mediante eventos.

Requisitos:
    - Tener instalada la librería PyQt5.

Componentes de la interfaz:
    - Una ventana principal con un título personalizado.
    - Un QLabel con texto estilizado.
    - Un QPushButton que imprime un mensaje en la consola al presionarlo.
    - Un QSlider que muestra su valor en la consola cuando se desliza.

"""

import os

# Configuración de la variable de entorno para PyQt5 en macOS
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

# Importamos los módulos necesarios de PyQt5
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QSlider
from PyQt5.QtCore import Qt

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
        self.w = 600  # Ancho de la ventana
        self.h = 300  # Alto de la ventana
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

        # Creamos un QLabel (Etiqueta) para mostrar texto en la interfaz
        label = QLabel("PROTOTIPO - I", self)
        label.move(230, 100)  # Posicionamos la etiqueta dentro de la ventana

        # Definimos el estilo de la etiqueta con CSS
        estilo_label = "font-size: 20px; color: orange"
        label.setStyleSheet(estilo_label)

        # Creamos un QPushButton (Botón)
        boton1 = QPushButton("ACTIVAR", self)
        boton1.move(250, 150)  # Posicionamos el botón dentro de la ventana

        # Conectamos el botón con el método 'activar' que se ejecutará al hacer clic
        boton1.clicked.connect(self.activar)

        # Creamos un QSlider (deslizador) con orientación horizontal
        slider = QSlider(Qt.Horizontal, self)
        slider.setGeometry(230, 200, 200, 30)  # Establecemos su tamaño y posición

        # Conectamos el slider con el método 'datos', que se ejecuta cuando cambia su valor
        slider.valueChanged.connect(self.datos)

        # Mostramos la ventana con todos los elementos
        self.show()

    def activar(self):
        """
        Método que se ejecuta cuando se presiona el botón 'ACTIVAR'.
        Imprime un mensaje en la consola.
        """
        print("Activado")

    def datos(self, data):
        """
        Método que se ejecuta cuando se cambia el valor del slider.
        :param data: Valor actual del slider.
        """
        print(data)

# Bloque principal de ejecución
if __name__ == "__main__":
    # Creamos la aplicación Qt
    app = QApplication([])

    # Creamos una instancia de la clase App (nuestra interfaz gráfica)
    ex = App()

    # Ejecutamos el bucle de eventos de la aplicación
    app.exec_()

# Documentación de PyQt5
# help(PyQt5)

# Métodos utilizados:
# setGeometry(ax: int, ay: int, aw: int, ah: int) -> None  # Define la posición y tamaño de la ventana
# setWindowTitle(a0: typing.Optional[str]) -> None  # Establece el título de la ventana
# show() -> None  # Muestra la ventana en pantalla
