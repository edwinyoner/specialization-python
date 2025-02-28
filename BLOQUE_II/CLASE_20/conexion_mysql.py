"""
Archivo: conexion_mysql.py
Autor: Edwin Yoner
Fecha: 24/02/2025

Descripción:
    Este script establece una conexión con una base de datos MySQL utilizando la librería `pymysql`.
    Se realiza una consulta para obtener la versión del servidor MySQL y se muestra en consola.

Requisitos:
    - Tener MySQL instalado y en ejecución.
    - Instalar la librería `pymysql` (`pip install pymysql`).
    - Configurar correctamente los parámetros de conexión.

Manejo de errores:
    - Se captura cualquier error de conexión o de ejecución de la consulta y se muestra en consola.
"""

import pymysql

# Configuración de conexión a MySQL
config = {
    "host": "localhost",  # Cambia si tu servidor MySQL está en otro host
    "user": "root",       # Usuario por defecto en XAMPP/WAMP
    "password": "",       # Si tienes contraseña, colócala aquí
    "database": "monitoreo"  # Cambia esto por el nombre de tu base de datos
}

try:
    # Establecer conexión con MySQL
    with pymysql.connect(**config) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
            print(f"Conectado a MySQL, versión: {version[0]} ")

except pymysql.MySQLError as e:
    print(f"Error al conectar a MySQL: {e}")
