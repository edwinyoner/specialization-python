"""
Archivo: archivos.py
Autor: Edwin Yoner
Fecha: 20/02/2025

Descripción:
    Este programa demuestra dos formas de leer un archivo de texto en Python:
    - Usando `open()` y `close()`.
    - Usando la estructura `with open()`, que maneja automáticamente el cierre del archivo.

Requisitos:
    - Debe existir un archivo llamado "datos.txt" en el mismo directorio del script.
"""

# Apertura y lectura manual del archivo con `open()` y `close()`
r = open("datos.txt", 'r')  # Abre el archivo en modo lectura ('r')
print(r.read())  # Lee y muestra el contenido del archivo
r.close()  # Cierra el archivo manualmente

print("***********")  # Separador visual

# Apertura y lectura usando `with open()`, que maneja el cierre automáticamente
with open("datos.txt", 'r') as r:
    print(r.read())  # Lee y muestra el contenido del archivo
