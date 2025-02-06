"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 30/01/2025

Descripción:
    Este programa muestra el uso de estructuras por comprensión en Python para listas.
    Se incluyen versiones tradicionales y optimizadas utilizando list comprehension.
"""

# 📌 Filtrar números pares en una lista (Versión tradicional)
lista = [1, 2, 3, 4, 5, 6, 1, 10, 8]
lista_pares = []
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
print("Números pares (versión tradicional):", lista_pares)

# 📌 Filtrar números pares con comprensión de listas
lista_pares_comp = [x for x in lista if x % 2 == 0]
print("Números pares (list comprehension):", lista_pares_comp)

# 📌 Filtrar números pares usando list()
lista_pares_list = list(x for x in lista if x % 2 == 0)
print("Números pares (con list()):", lista_pares_list)

print("\n")

# 📌 Capitalizar elementos de una lista (Versión tradicional)
paises = ["peru", "mexico", "ecuador", "colombia", "bolivia"]
for i in range(len(paises)):
    paises[i] = paises[i].capitalize()
print("Lista de países capitalizados (versión tradicional):", paises)

# 📌 Capitalizar elementos de una lista con comprensión de listas
paises_comp = [i.capitalize() for i in paises]
print("Lista de países capitalizados (list comprehension):", paises_comp)

# 📌 Capitalizar elementos usando list()
paises_list = list(i.capitalize() for i in paises)
print("Lista de países capitalizados (con list()):", paises_list)

print("\n")

# 📌 Filtrar frutas que comienzan con 'm' (Versión tradicional)
frutas = ["manzana", "pera", "melon", "sandia", "mandarina"]
frutas_m = []
for i in frutas:
    if i[0] == "m":
        frutas_m.append(i)
print("Frutas que comienzan con 'm' (versión tradicional):", frutas_m)

# 📌 Filtrar frutas con comprensión de listas
frutas_m_comp = [i for i in frutas if i[0] == "m"]
print("Frutas que comienzan con 'm' (list comprehension):", frutas_m_comp)

# 📌 Filtrar frutas usando list()
frutas_m_list = list(i for i in frutas if i[0] == "m")
print("Frutas que comienzan con 'm' (con list()):", frutas_m_list)

print("\n")

# 📌 Filtrar números positivos en una lista (Versión tradicional)
numeros = [-1, 2, 8, -6, -4, 10, 12]
positivos = []
for i in numeros:
    if i > 0:
        positivos.append(i)
print("Números positivos (versión tradicional):", positivos)

# 📌 Filtrar números positivos con comprensión de listas
positivos_comp = [i for i in numeros if i > 0]
print("Números positivos (list comprehension):", positivos_comp)

# 📌 Filtrar números positivos usando list()
positivos_list = list(i for i in numeros if i > 0)
print("Números positivos (con list()):", positivos_list)