"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 30/01/2025

Descripción:
    Este programa demuestra el uso del bucle `for` en Python con diferentes estructuras 
    de datos y condiciones. Se incluyen ejemplos de iteración sobre rangos y listas, 
    manipulación de cadenas y filtrado de elementos en listas.
"""

# Imprimir números pares del 0 al 9 usando un condicional dentro del bucle
print("Números pares del 0 al 9:")
for i in range(10):
    if i % 2 == 0:
        print(i)

print("\n")

# Imprimir números pares del 0 al 18 usando un rango con paso de 2
print("Números pares del 0 al 18:")
for i in range(0, 20, 2):
    print(i)

print("\n")

# Capitalizar cada elemento de una lista de países
paises = ["peru", "mexico", "ecuador", "colombia", "bolivia"]
print("Lista de países con la primera letra en mayúscula:")
for i in range(len(paises)):
    paises[i] = paises[i].capitalize()
print(paises)

print("\n")

# Filtrar frutas que comiencen con la letra 'm' (Versión original)
frutas = ["manzana", "pera", "melon", "sandia", "mandarina"]
frutas_con_m = []
for i in frutas:
    if i[0] == "m":
        frutas_con_m.append(i)
print("Frutas que comienzan con 'm' (versión original):")
print(frutas_con_m)

print("\n")

# Filtrar frutas que comiencen con la letra 'm' (Versión optimizada con comprensión de listas)
frutas_con_m_opt = [fruta for fruta in frutas if fruta.startswith("m")]
print("Frutas que comienzan con 'm' (versión optimizada):")
print(frutas_con_m_opt)