"""
Archivo: insertar_datos_mysql.py
Autor: Edwin Yoner
Fecha: 24/02/2025

Descripción:
    Este script inserta datos de temperatura y humedad en la base de datos MySQL.
    Los valores son almacenados en la tabla `sensores` con una marca de tiempo automática.

Requisitos:
    - Tener MySQL instalado y en ejecución.
    - Instalar la librería `pymysql` (`pip install pymysql`).
    - Configurar correctamente los parámetros de conexión y la estructura de la tabla.

Estructura de la tabla `sensores` en MySQL:
    CREATE TABLE sensores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tiempo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        temperatura INT,
        humedad INT
    );

Manejo de errores:
    - Se captura cualquier error de conexión o de ejecución de la consulta y se muestra en consola.
"""

import pymysql

# Valores de temperatura y humedad a insertar
temp = 15
humi = 45

# Configuración de conexión a MySQL
config = {
    "host": "localhost",  # Cambiar si el servidor MySQL está en otro host
    "user": "root",  # Usuario por defecto en XAMPP/WAMP
    "password": "",  # Si tienes contraseña, colócala aquí
    "database": "monitoreo"  # Cambiar por el nombre de la base de datos
}

try:
    # Establecer conexión con MySQL
    with pymysql.connect(**config) as con:
        with con.cursor() as cursor:
            # Query SQL para insertar los datos
            insert_query = "INSERT INTO sensores (id, tiempo, temperatura, humedad) VALUES (NULL, current_timestamp(), %s, %s);"

            # Ejecutar consulta con parámetros para evitar inyección SQL
            cursor.execute(insert_query, (temp, humi))

            # Confirmar cambios en la base de datos
            con.commit()
            print("Datos insertados correctamente en la tabla `sensores`.")

except pymysql.MySQLError as e:
    print(f"Error al conectar o insertar datos en MySQL: {e}")


"""
con = pymysql.connect(user="root",password = "", host="localhost", database="monitoreo")
c = con.cursor()
insert_query = f"INSERT INTO sensores (id,tiempo,temperatura,humedad) VALUES (NULL, current_timestamp(),{temp},{humi});"
c.execute(insert_query)
con.commit()
c.close()
con.close()
"""
