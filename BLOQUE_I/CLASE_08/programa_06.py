"""
Archivo: programa_06.py
Autor: Edwin Yoner
Fecha: 30/01/2025

Descripción:
    Este programa demuestra el uso de estructuras por comprensión en diccionarios en Python, 
    mostrando ejemplos de generación y filtrado de elementos.
"""

# 📌 Creación de un diccionario con claves y valores generados dinámicamente (versión tradicional)
a = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
print("Diccionario original:", a)

# 📌 Creación de un diccionario usando comprensión de diccionarios
a_comp = {x: 2 * x for x in range(5)}
print("Diccionario generado con comprensión:", a_comp)

# 📌 Diccionario de frutas con claves personalizadas
frutas = {
    "f1": "manzana",
    "f2": "pera",
    "f3": "melon",
    "f4": "sandia",
    "45": "mandarina"
}
print("Diccionario de frutas:", frutas)

# 📌 Creación de un nuevo diccionario que filtra solo las frutas cuyos valores empiezan con 'm'
frutas1 = {clave: valor for clave, valor in frutas.items() if valor[0] == "m"}
print("Frutas que empiezan con 'm':", frutas1)