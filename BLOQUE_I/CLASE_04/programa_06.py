"""
Archivo: programa_06.py
Autor: Edwin Yoner
Fecha: 21/01/2025

Descripción:
    Este programa muestra cómo manipular diccionarios (Mapping) en Python,
    incluyendo indexación, copia, eliminación de elementos y acceso a claves y valores.
"""

# Definición de un diccionario con claves y valores
x = {"C": 99, "Python": 3.8, "PHP": 7}

# Indexación en diccionarios (acceso a valores mediante claves)
print("Valor de 'C':", x["C"])  # 99
print("Valor de 'Python':", x["Python"])  # 3.8
print("Valor de 'PHP':", x["PHP"])  # 7

# Métodos de Diccionarios

# Método copy() y clear()
# Se crea una copia del diccionario y se limpia
y = x.copy()  # Copia del diccionario original
y.clear()  # Se vacía el diccionario copiado
print("Diccionario copiado y vacío:", y)  # {}
print("Diccionario original sin cambios:", x)  # {'C': 99, 'Python': 3.8, 'PHP': 7}

# Agregar un nuevo elemento al diccionario
x["C++"] = 2017
print("Diccionario después de agregar 'C++':", x)  # {'C': 99, 'Python': 3.8, 'PHP': 7, 'C++': 2017}

# Método pop(): Elimina un elemento y devuelve su valor
y = x.pop("C++")
print("Elemento eliminado ('C++'):", y)  # 2017
print("Diccionario después de eliminar 'C++':", x)  # {'C': 99, 'Python': 3.8, 'PHP': 7}

# Método items(): Devuelve una vista de los pares clave-valor
y = x.items()
print("Elementos del diccionario:", y)  # dict_items([('C', 99), ('Python', 3.8), ('PHP', 7)])

# Método keys(): Devuelve una vista de las claves del diccionario
y = x.keys()
print("Claves del diccionario:", y)  # dict_keys(['C', 'Python', 'PHP'])

# Método values(): Devuelve una vista de los valores del diccionario
y = x.values()
print("Valores del diccionario:", y)  # dict_values([99, 3.8, 7])

# Diccionario con listas como valores
objetos = {
    "oficina": ["lapicero", "cuaderno"],
    "cocina": ["sarten", "cuchara"]
}

# Acceso a elementos dentro de listas en un diccionario
print("Primer elemento de 'oficina':", objetos["oficina"][0])  # lapicero
print("Segundo elemento de 'cocina':", objetos["cocina"][1])  # cuchara

# Método clear() para vaciar el diccionario
objetos.clear()
print("Diccionario 'objetos' después de clear():", objetos)  # {}
