"""
Archivo: app_mysql_pyqt5.py
Autor: Edwin Yoner
Fecha: 24/02/2025

Descripción:
    Este script crea una aplicación en PyQt5 que permite insertar y visualizar
    datos de temperatura y humedad desde una base de datos MySQL.
    Los valores se actualizan automáticamente cada segundo y se muestran en la interfaz.

Requisitos:
    - Tener MySQL instalado y en ejecución.
    - Instalar las librerías necesarias:
      `pip install pymysql PyQt5`
    - Configurar correctamente los parámetros de conexión y asegurarse de que la estructura de la tabla
      coincida con la esperada.

Estructura de la tabla `sensores` en MySQL:
    CREATE TABLE sensores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tiempo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        temperatura INT,
        humedad INT
    );

Manejo de errores:
    - Se recomienda manejar excepciones al conectar con la base de datos y al ejecutar consultas.
"""

import os

# Configuración de la variable de entorno para PyQt5 en macOS
os.environ[
    "QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

# Importación de PyQt5 para la interfaz gráfica
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import QTimer

# Importación de pymysql para la conexión con MySQL
import pymysql


class App(QWidget):
    """
    Clase principal de la aplicación que permite insertar y visualizar
    datos en la base de datos MySQL desde una interfaz gráfica en PyQt5.
    """

    def __init__(self):
        super().__init__()
        self.w = 300  # Ancho de la ventana
        self.h = 200  # Alto de la ventana
        self.x = 100  # Posición X de la ventana
        self.y = 100  # Posición Y de la ventana
        self.titulo = "PROYECTO"  # Título de la ventana
        self.initUI()  # Inicializa la interfaz

    def initUI(self):
        """
        Configura la interfaz gráfica de la aplicación, incluyendo un botón para insertar datos
        y un QLabel para mostrar los valores más recientes de la base de datos.
        """
        self.setGeometry(self.x, self.y, self.w, self.h)  # Establece el tamaño y posición de la ventana
        self.setWindowTitle(self.titulo)  # Asigna el título a la ventana

        # Creación del botón para insertar datos manualmente
        b1 = QPushButton("Insertar", self)
        b1.setGeometry(100, 100, 80, 30)  # Posición y tamaño del botón
        b1.clicked.connect(self.mysql_query)  # Conecta el botón con la función mysql_query

        # Creación de un temporizador que actualiza los datos en la interfaz cada segundo
        timer = QTimer(self)
        timer.timeout.connect(self.datos)  # Conecta el temporizador con la función datos
        timer.start(1000)  # Intervalo de actualización: 1 segundo

        # QLabel para mostrar la temperatura y humedad obtenida de la base de datos
        self.label = QLabel("Esperando datos ...", self)
        self.label.setGeometry(100, 50, 200, 30)  # Posición y tamaño del QLabel

        self.show()  # Muestra la ventana

    def datos(self):
        """
        Obtiene el último registro de la tabla `sensores` en la base de datos y actualiza
        la etiqueta con los valores de temperatura y humedad.
        """
        con = pymysql.connect(
            user="root",  # Usuario de MySQL
            password="",  # Contraseña (vacía por defecto en XAMPP/WAMP)
            host="localhost",  # Servidor local
            database="monitoreo"  # Nombre de la base de datos
        )
        c = con.cursor()  # Crea un cursor para ejecutar consultas SQL

        # Consulta SQL para obtener el último registro insertado en la tabla `sensores`
        insert_query = "SELECT * FROM sensores ORDER BY id DESC LIMIT 1;"
        c.execute(insert_query)
        r = c.fetchone()  # Obtiene la primera fila del resultado

        c.close()
        con.close()

        # Si hay un resultado, se actualiza el QLabel con los valores de temperatura y humedad
        if r:
            temp = r[2]
            humi = r[3]
            self.label.setText(str(temp) + "    " + str(humi))

    def mysql_query(self):
        """
        Inserta un nuevo registro en la base de datos con valores fijos de temperatura y humedad.
        """
        con = pymysql.connect(
            user="root",  # Usuario de MySQL
            password="",  # Contraseña (vacía por defecto en XAMPP/WAMP)
            host="localhost",  # Servidor local
            database="monitoreo"  # Nombre de la base de datos
        )
        c = con.cursor()  # Crea un cursor para ejecutar consultas SQL

        # Valores simulados de temperatura y humedad
        temp = 26
        humi = 90

        # Consulta SQL para insertar los datos en la tabla `sensores`
        insert_query = f"INSERT INTO sensores (id, tiempo, temperatura, humedad) VALUES (NULL, current_timestamp(), {temp}, {humi});"

        c.execute(insert_query)  # Ejecuta la consulta
        con.commit()  # Guarda los cambios en la base de datos

        c.close()
        con.close()


if __name__ == "__main__":
    # Creación de la aplicación PyQt5
    app = QApplication([])
    ex = App()  # Instancia de la clase App
    app.exec_()  # Inicia el bucle de eventos de la aplicación
