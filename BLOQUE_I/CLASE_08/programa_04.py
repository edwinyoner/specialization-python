"""
Archivo: programa_04.py
Autor: Edwin Yoner
Fecha: 30/01/2025

Descripción:
    Este programa demuestra el uso de comprensión de conjuntos en Python.
    Se incluyen diferentes formas de generar conjuntos de manera eficiente.
"""

# Estructuras por comprensión - Conjuntos

# Definir un conjunto de números del 0 al 7 (Forma explícita)
conjunto1 = {0, 1, 2, 3, 4, 5, 6, 7}
print("Conjunto definido explícitamente:", conjunto1)

# Generar un conjunto usando comprensión de conjuntos
conjunto2 = {x for x in range(8)}
print("Conjunto generado con comprensión:", conjunto2)

# Generar un conjunto usando la función `set()` y comprensión de conjuntos
conjunto3 = set(x for x in range(8))
print("Conjunto generado con `set()` y comprensión:", conjunto3)

# Verificar que todos los conjuntos son iguales
print("¿Todos los conjuntos son iguales?", conjunto1 == conjunto2 == conjunto3)
