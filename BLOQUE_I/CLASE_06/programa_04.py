"""
Archivo: programa_04.py
Autor: Edwin Yoner
Fecha: 25/01/2025

Descripción:
    Este programa solicita dos notas al usuario, verifica que sean valores válidos,
    calcula el promedio y muestra el resultado en pantalla.
"""

# Función para solicitar una nota con validación
def obtener_nota(numero):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero}: "))
            if 0 <= nota <= 20:  # Se asume una escala de 0 a 20
                return nota
            else:
                print("Error: La nota debe estar entre 0 y 20.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Obtener notas con validación
nota1 = obtener_nota(1)
nota2 = obtener_nota(2)

# Calcular el promedio
promedio = (nota1 + nota2) / 2

# Mostrar el resultado
print(f"El promedio de las notas {nota1} y {nota2} es: {promedio:.2f}")  # Formato con 2 decimales