"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 23/01/2025

Descripción:
    Este programa demuestra el uso de conjuntos en Python, incluyendo 
    operaciones como unión, intersección y diferencia.
"""

# Definición de conjuntos
conjunto_a = {2, 8, 9, 1, 1}  # Se eliminan los duplicados automáticamente
conjunto_b = {2, 4, 9, 0, 6}

# Mostrar el tipo de dato
print(f"Tipo de dato de conjunto_a: {type(conjunto_a)}")

# Unión de conjuntos: combina elementos de ambos conjuntos sin duplicados
union_conjuntos = conjunto_a.union(conjunto_b)
print(f"Unión: {union_conjuntos}")
print(f"Tamaño de la unión: {len(union_conjuntos)}")

# Intersección de conjuntos: elementos comunes entre ambos conjuntos
interseccion_conjuntos = conjunto_a.intersection(conjunto_b)
print(f"Intersección: {interseccion_conjuntos}")
print(f"Tamaño de la intersección: {len(interseccion_conjuntos)}")

# Diferencia de conjuntos: elementos que están en A pero no en B
diferencia_a_b = conjunto_a.difference(conjunto_b)
print(f"Diferencia A - B: {diferencia_a_b}")
print(f"Tamaño de la diferencia A - B: {len(diferencia_a_b)}")

# Diferencia de conjuntos: elementos que están en B pero no en A
diferencia_b_a = conjunto_b.difference(conjunto_a)
print(f"Diferencia B - A: {diferencia_b_a}")
print(f"Tamaño de la diferencia B - A: {len(diferencia_b_a)}")
