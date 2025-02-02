"""
Archivo: programa_05.py
Autor: Edwin Yoner
Fecha: 25/01/2025

Descripción:
    Este programa calcula el área y el perímetro de un rectángulo 
    a partir de la base y la altura ingresadas por el usuario.
"""

def calcular_area_perimetro(base, altura):
    """
    Calcula el área y el perímetro de un rectángulo.

    Parámetros:
    - base (float): Longitud de la base del rectángulo.
    - altura (float): Longitud de la altura del rectángulo.

    Retorna:
    - area (float): Área del rectángulo.
    - perimetro (float): Perímetro del rectángulo.
    """
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

# Solicitar datos al usuario
base = float(input("Ingrese la medida de la base: "))
altura = float(input("Ingrese la medida de la altura: "))

# Llamar a la función para calcular área y perímetro
area, perimetro = calcular_area_perimetro(base, altura)

# Mostrar resultados
print(f"El área es: {area}")
print(f"El perímetro es: {perimetro}")