"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 25/01/2025

Descripción:
    Este programa solicita dos números al usuario, los convierte a enteros y 
    muestra el resultado de su suma. Se incluyen validaciones para evitar errores.
"""

# Solicitar números al usuario con validación
while True:
    try:
        num1 = int(input("Ingrese el primer número: "))  # Conversión directa a entero
        break
    except ValueError:
        print("Error: Debe ingresar un número válido.")

while True:
    try:
        num2 = int(input("Ingrese el segundo número: "))  # Conversión directa a entero
        break
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Realizar la suma
resultado = num1 + num2

# Mostrar el resultado
print(f"La suma de {num1} y {num2} es: {resultado}")