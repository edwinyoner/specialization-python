"""
Archivo: programa_07.py
Autor: Edwin Yoner
Fecha: 30/01/2025

Descripción:
    Este programa toma un diccionario de frutas y genera un nuevo diccionario 
    que solo contiene aquellas frutas cuyos nombres comienzan con la letra 'm', 
    utilizando comprensión de diccionarios.
"""

# Diccionario original de frutas
frutas = {
    "f1": "manzana",
    "f2": "pera",
    "f3": "melon",
    "f4": "sandia",
    "45": "mandarina"
}

# Generar un nuevo diccionario con frutas que comiencen con 'm'
frutas_con_m = {clave: valor for clave, valor in frutas.items() if valor.startswith("m")}

# Mostrar resultado
print("Diccionario original:", frutas)
print("Frutas que comienzan con 'm':", frutas_con_m)