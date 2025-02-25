"""
Archivo: ventana.py
Autor: Edwin Yoner
Fecha: 20/02/2025

Descripción:
    Este programa crea una interfaz gráfica básica utilizando PyQt5.
    Contiene un QLabel (etiqueta), un QPushButton (botón), un QSlider (deslizador)
    y una QProgressBar (barra de progreso). Se maneja la interacción con botones
    y el slider mediante eventos.

Requisitos:
    - Tener instalada la librería PyQt5.

Componentes de la interfaz:
    - Una ventana principal con un título personalizado.
    - Un QLabel con texto estilizado que cambia al activar/desactivar.
    - Un QPushButton para activar y otro para desactivar.
    - Un QSlider que actualiza un QLabel y una QProgressBar.
    - Una QProgressBar que muestra el valor del slider.
"""

import os

# Configuración de la variable de entorno para PyQt5 en macOS
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

# Importamos los módulos necesarios de PyQt5
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QSlider, QProgressBar
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
        self.h = 500  # Alto de la ventana
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

        # Creamos un QLabel (Etiqueta) para mostrar un título
        self.label1 = QLabel("PROTOTIPO - I", self)
        self.label1.move(230, 100)  # Posicionamos la etiqueta dentro de la ventana

        # Definimos el estilo de la etiqueta con CSS
        estilo_label = "font-size: 20px; color: orange"
        self.label1.setStyleSheet(estilo_label)

        # Creamos otro QLabel para mostrar el valor del slider
        self.label2 = QLabel("VALOR: 0", self)
        self.label2.move(230, 230)  # Posicionamos la etiqueta dentro de la ventana
        self.label2.setStyleSheet(estilo_label)  # Aplicamos el mismo estilo

        # Creamos un QPushButton (Botón de Activar)
        boton1 = QPushButton("ACTIVAR", self)
        boton1.move(200, 150)  # Posicionamos el botón en la ventana

        # Conectamos el botón con el método 'activar'
        boton1.clicked.connect(self.activar)

        # Creamos un QPushButton (Botón de Desactivar)
        boton2 = QPushButton("DESACTIVAR", self)
        boton2.move(300, 150)  # Posicionamos el botón en la ventana

        # Conectamos el botón con el método 'desactivar'
        boton2.clicked.connect(self.desactivar)

        # Creamos un QSlider (deslizador) con orientación horizontal
        slider = QSlider(Qt.Horizontal, self)
        slider.setGeometry(230, 200, 200, 30)  # Establecemos su tamaño y posición
        slider.setMinimum(0)  # Valor mínimo del slider
        slider.setMaximum(100)  # Valor máximo del slider

        # Conectamos el slider con el método 'datos', que se ejecuta cuando cambia su valor
        slider.valueChanged.connect(self.datos)

        # Creamos una QProgressBar (Barra de progreso)
        self.bar = QProgressBar(self)
        self.bar.setGeometry(230, 250, 200, 30)  # Establecemos su tamaño y posición
        self.bar.setValue(0)  # Inicializamos la barra en 0

        # Mostramos la ventana con todos los elementos
        self.show()

    def activar(self):
        """
        Método que se ejecuta cuando se presiona el botón 'ACTIVAR'.
        - Cambia el texto del label1 a 'Activado'.
        - Ajusta el tamaño del texto para que se visualice correctamente.
        """
        print("Activado")
        self.label1.setText("Activado")
        self.label1.adjustSize()

    def desactivar(self):
        """
        Método que se ejecuta cuando se presiona el botón 'DESACTIVAR'.
        - Cambia el texto del label1 a 'Desactivado'.
        - Ajusta el tamaño del texto para que se visualice correctamente.
        """
        print("Desactivado")
        self.label1.setText("Desactivado")
        self.label1.adjustSize()

    def datos(self, data):
        """
        Método que se ejecuta cuando se cambia el valor del slider.
        - Muestra el valor del slider en la etiqueta label2.
        - Ajusta el tamaño del texto para que se visualice correctamente.
        - Actualiza la barra de progreso con el mismo valor del slider.

        :param data: Valor actual del slider.
        """
        print(data)
        self.label2.setText("Valor: " + str(data))
        self.label2.adjustSize()
        self.bar.setValue(data)

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
