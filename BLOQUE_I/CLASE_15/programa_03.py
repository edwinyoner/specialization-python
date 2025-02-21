"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este módulo contiene diversas operaciones con listas en Python utilizando funciones lambda,
    `map`, `filter` y listas por comprensión. Se incluyen operaciones para obtener valores absolutos,
    filtrar números negativos o positivos, calcular cubos de números positivos y manipular cadenas.
"""

# Lista de números con valores negativos y positivos
numeros = [-1, 2, -3, 4, -5, -6, -7, 8]

# 1. Obtener el valor absoluto de cada número en la lista

# Usando `map` con `lambda`
modulo_map = list(map(abs, numeros))
print("1. Módulo con map:", modulo_map)

# Usando listas por comprensión
modulo_comprension = [abs(numero) for numero in numeros]
print("2. Módulo con listas por comprensión:", modulo_comprension)

# 2. Filtrar números negativos

# Usando `lambda` y listas por comprensión
numeros_negativos = list(filter(lambda numero: numero < 0, numeros))
print("3. Números negativos con filter:", numeros_negativos)

# Usando listas por comprensión
numeros_negativos_comprension = [numero for numero in numeros if numero < 0]
print("4. Números negativos con listas por comprensión:", numeros_negativos_comprension)

# 3. Filtrar números positivos

# Usando `filter` con `lambda`
numeros_positivos = list(filter(lambda numero: numero >= 0, numeros))
print("5. Números positivos con filter:", numeros_positivos)

# Usando listas por comprensión
numeros_positivos_comprension = [numero for numero in numeros if numero >= 0]
print("6. Números positivos con listas por comprensión:", numeros_positivos_comprension)

# 4. Calcular los cubos de los números positivos

# Lista de prueba
numeros_b = [1, -2, 5, -3, 7]

# Usando listas por comprensión
cubos_positivos_comprension = [numero ** 3 for numero in numeros_b if numero ** 3 > 0]
print("7. Cubos positivos con listas por comprensión:", cubos_positivos_comprension)

# Usando `map` y `filter`
cubos_todos = list(map(lambda numero: numero ** 3, numeros_b))  # Calcula el cubo de todos
cubos_filtrados = list(filter(lambda cubo: cubo > 0, cubos_todos))  # Filtra solo los positivos
print("8. Cubos positivos con map y filter:", cubos_filtrados)

# 5. Convertir palabras a mayúsculas y filtrar las que empiezan con 'P'

# Lista de palabras
palabras = ["perro", "gato", "pelota", "manzana", "libro", "python"]

# Usando `map` y `filter`
palabras_mayusculas = list(map(str.upper, filter(lambda palabra: palabra.startswith('p'), palabras)))
print("9. Palabras en mayúsculas que empiezan con 'P' (map + filter):", palabras_mayusculas)

# Usando listas por comprensión
palabras_mayusculas_comprension = [palabra.upper() for palabra in palabras if palabra.startswith("p")]
print("10. Palabras en mayúsculas que empiezan con 'P' (listas por comprensión):", palabras_mayusculas_comprension)