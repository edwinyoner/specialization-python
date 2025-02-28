import numpy as np

lista1 = [2, 3, 4]
lista2 = [2, 6, 3]

v1 = np.array(lista1)
v2 = np.array(lista2)
#print(v1)
#print(v2)
#Operaciones Básicas
v3 = v1 + v2
print(v3)

v4 = v1 - v2
print(v4)

v5 = v1 * v2
print(v5)

v6 = v1 / v2
print(v6)

v7 = v1 ** 2
print(v7)

v8 = v1 % v2
print(v8)

v9 = v1 // v2
print(v9)

# Producto escalar
producto_escalar = np.dot(v1, v2)

# Producto vectorial
producto_vectorial = np.cross(v1, v2)

# Imprimir resultados
print("Producto escalar:", producto_escalar)
print("Producto vectorial:", producto_vectorial)