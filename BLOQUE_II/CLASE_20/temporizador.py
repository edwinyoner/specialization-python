"""""
Archivo: temporizador.py
Autor: Edwin Yoner
Fecha: 24/02/2025

Descripción:
    Este script crea una aplicación en PyQt5 que inserta datos de temperatura y humedad
    en una base de datos MySQL de manera automática cada 20 segundos.
    Los valores se almacenan en la tabla `sensores` con una marca de tiempo automática.

Tecnologías utilizadas:
- PyQt5: Para la interfaz gráfica.
- pymysql: Para la conexión y manipulación de la base de datos MySQL.

Requisitos previos:
- Tener un servidor MySQL en funcionamiento (por ejemplo, XAMPP o WAMP).
- Base de datos 'monitoreo' con una tabla 'sensores' que contenga las columnas:
  (id INT AUTO_INCREMENT PRIMARY KEY, tiempo TIMESTAMP, temperatura FLOAT, humedad FLOAT).
"""

import os

# Configuración de la variable de entorno para PyQt5 en macOS
# Esto es necesario si PyQt5 no encuentra los plugins de la plataforma.
os.environ[
    "QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

# Importación de PyQt5 para la interfaz gráfica
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer

# Importación de pymysql para la conexión con MySQL
import pymysql


class App(QWidget):
    """
    Clase principal de la aplicación que crea una ventana y ejecuta
    una consulta MySQL cada 20 segundos para insertar datos en la base de datos.
    """

    def __init__(self):
        super().__init__()
        self.w = 300  # Ancho de la ventana
        self.h = 200  # Alto de la ventana
        self.x = 100  # Posición X de la ventana
        self.y = 100  # Posición Y de la ventana
        self.titulo = "PROYECTO"  # Título de la ventana
        self.initUI()  # Llamada al método que inicializa la interfaz

    def initUI(self):
        """
        Configura la interfaz gráfica de la aplicación y
        establece un temporizador que ejecuta una consulta MySQL periódicamente.
        """
        self.setGeometry(self.x, self.y, self.w, self.h)  # Establece el tamaño y posición de la ventana
        self.setWindowTitle(self.titulo)  # Asigna el título a la ventana

        # Creación de un temporizador
        timer = QTimer(self)
        timer.timeout.connect(self.mysql_query)  # Conecta el temporizador con la función mysql_query
        timer.start(20000)  # Ejecuta la consulta cada 20 segundos

        self.show()  # Muestra la ventana

    def mysql_query(self):
        """
        Conecta a la base de datos MySQL y ejecuta una consulta para insertar datos
        en la tabla `sensores`.
        """
        # Conexión a la base de datos MySQL
        con = pymysql.connect(
            user="root",  # Usuario de MySQL
            password="",  # Contraseña (vacía por defecto en XAMPP/WAMP)
            host="localhost",  # Servidor local
            database="monitoreo"  # Nombre de la base de datos
        )
        c = con.cursor()  # Crea un cursor para ejecutar consultas SQL

        # Datos de temperatura y humedad simulados
        temp = 22
        humi = 88

        # Consulta SQL para insertar datos en la tabla `sensores`
        insert_query = f"""
        INSERT INTO sensores (id, tiempo, temperatura, humedad) 
        VALUES (NULL, current_timestamp(), {temp}, {humi});
        """

        c.execute(insert_query)  # Ejecuta la consulta
        con.commit()  # Guarda los cambios en la base de datos

        # Cierre de la conexión
        c.close()
        con.close()


if __name__ == "__main__":
    # Creación de la aplicación
    app = QApplication([])
    ex = App()  # Instancia de la clase App
    app.exec_()  # Inicia el bucle de eventos de la aplicación
