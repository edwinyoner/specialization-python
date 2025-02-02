"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 25/01/2025

Descripción:
    Este programa demuestra el uso de los diferentes tipos de operadores en Python,
    incluyendo aritméticos, relacionales, lógicos, de asignación, de identidad y de pertenencia.
"""

# Operadores Aritméticos
# Se utilizan para realizar operaciones matemáticas básicas

a = 10
b = 3

print("Operadores Aritméticos:")
print(f"Suma: {a} + {b} = {a + b}")         # Suma
print(f"Resta: {a} - {b} = {a - b}")        # Resta
print(f"Multiplicación: {a} * {b} = {a * b}")  # Multiplicación
print(f"División: {a} / {b} = {a / b}")     # División
print(f"División entera: {a} // {b} = {a // b}") # División entera
print(f"Módulo: {a} % {b} = {a % b}")       # Módulo
print(f"Potencia: {a} ** {b} = {a ** b}")   # Potencia

# Alternativa con métodos especiales
print(f"Suma con método especial: {a.__add__(b)}")  # Alternativa a `a + b`

print("\nOperadores Relacionales:")
# Operadores Relacionales (Comparación)
# Se utilizan para comparar valores y devuelven un resultado booleano (True o False)

print(f"{a} > {b}: {a > b}")    # Mayor que
print(f"{a} < {b}: {a < b}")    # Menor que
print(f"{a} >= {b}: {a >= b}")  # Mayor o igual que
print(f"{a} <= {b}: {a <= b}")  # Menor o igual que
print(f"{a} == {b}: {a == b}")  # Igualdad
print(f"{a} != {b}: {a != b}")  # Diferente

print("\nOperadores Lógicos:")
# Operadores Lógicos
# Se utilizan para realizar operaciones lógicas

x = True
y = False

print(f"{x} and {y} = {x and y}")  # Operador AND
print(f"{x} or {y} = {x or y}")    # Operador OR
print(f"not {x} = {not x}")        # Operador NOT

print("\nOperadores de Asignación:")
# Operadores de Asignación
# Se utilizan para asignar valores a variables

c = 5
print(f"Valor inicial de c: {c}")

c += 2  # Equivalente a c = c + 2
print(f"c += 2 -> {c}")

c -= 1  # Equivalente a c = c - 1
print(f"c -= 1 -> {c}")

c *= 3  # Equivalente a c = c * 3
print(f"c *= 3 -> {c}")

c /= 2  # Equivalente a c = c / 2
print(f"c /= 2 -> {c}")

c //= 2  # Equivalente a c = c // 2
print(f"c //= 2 -> {c}")

c %= 2  # Equivalente a c = c % 2
print(f"c %= 2 -> {c}")

c **= 3  # Equivalente a c = c ** 3
print(f"c **= 3 -> {c}")

print("\nOperadores de Identidad:")
# Operadores de Identidad
# Se utilizan para comparar si dos variables hacen referencia al mismo objeto en memoria

d = [1, 2, 3]
e = d
f = [1, 2, 3]

print(f"d is e: {d is e}")  # True, porque apuntan al mismo objeto
print(f"d is not f: {d is not f}")  # True, porque son listas distintas aunque tengan el mismo contenido

print("\nOperadores de Pertenencia:")
# Operadores de Pertenencia
# Se utilizan para verificar si un valor está presente en una secuencia (listas, tuplas, cadenas, diccionarios)

frutas = ["manzana", "naranja", "pera"]

print(f"'manzana' in frutas: {'manzana' in frutas}")  # True
print(f"'banana' not in frutas: {'banana' not in frutas}")  # True