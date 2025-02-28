"""
Archivo: archivos_ventana.py
Autor: Edwin Yoner
Fecha: 22/02/2025

Descripción:
    Este programa crea una interfaz gráfica con PyQt5 que muestra dos barras de progreso
    y etiquetas para visualizar temperatura y humedad en tiempo real, leyendo datos desde
    un archivo `datos.txt`.

Requisitos:
    - Tener instalada la librería PyQt5.
    - Un archivo `datos.txt` con valores de temperatura y humedad en formato "temp,hum".

Componentes de la interfaz:
    - Una ventana principal con un título personalizado.
    - Dos QLabel que muestran la temperatura y la humedad.
    - Dos QProgressBar para visualizar temperatura y humedad.
    - Un QTimer que actualiza los valores cada segundo leyendo el archivo `datos.txt`.
"""

import os

# Configuración de la variable de entorno para PyQt5 en macOS
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

# Importamos los módulos necesarios de PyQt5
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QProgressBar
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

        # Creamos QLabel para mostrar la temperatura
        self.label1 = QLabel("Esperando...", self)
        self.label1.setGeometry(100, 150, 150, 30)  # Establecemos la posición y tamaño

        # Creamos QLabel para mostrar la humedad
        self.label2 = QLabel("Esperando...", self)
        self.label2.setGeometry(300, 150, 150, 30)  # Establecemos la posición y tamaño

        # Creamos la primera barra de progreso para temperatura
        self.bar1 = QProgressBar(self)
        self.bar1.setGeometry(100, 100, 100, 30)  # Establecemos la posición y tamaño

        # Creamos la segunda barra de progreso para humedad
        self.bar2 = QProgressBar(self)
        self.bar2.setGeometry(300, 100, 100, 30)  # Establecemos la posición y tamaño

        # Creamos un QTimer (Temporizador) para actualizar los valores periódicamente
        timer = QTimer(self)  # Inicializamos el temporizador
        timer.timeout.connect(self.mostrar_mensaje)  # Conectamos el temporizador al método
        timer.start(1000)  # Configuramos el temporizador para que se ejecute cada 1000ms (1 segundo)

        # Mostramos la ventana con todos los elementos
        self.show()

    def mostrar_mensaje(self):
        """
        Método que se ejecuta cada vez que el temporizador llega al timeout.
        - Lee la última línea del archivo `datos.txt`.
        - Extrae los valores de temperatura y humedad.
        - Actualiza los QLabel y las barras de progreso con los nuevos valores.
        """
        with open("datos.txt", "r") as f:
            lineas = f.readlines()[-1][:-1]  # Obtiene la última línea del archivo y elimina el salto de línea
            u_linea = lineas.strip()  # Elimina espacios en blanco adicionales
            temp = u_linea.split(",")[0]  # Extrae el valor de la temperatura
            humi = u_linea.split(",")[1]  # Extrae el valor de la humedad

            # Actualiza los QLabel con los nuevos valores
            self.label1.setText(temp)
            self.label2.setText(humi)

            # Actualiza las barras de progreso con los valores leídos
            self.bar1.setValue(int(temp))
            self.bar2.setValue(int(humi))

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
