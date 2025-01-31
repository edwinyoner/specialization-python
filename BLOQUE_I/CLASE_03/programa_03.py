"""
Archivo: programa_03.py
Autor: Edwin Yoner
Fecha: 18/01/2025

Descripción:
    Este programa explora diferentes métodos de listas en Python, 
    incluyendo clear, copy, append, insert y pop.
"""

# Método clear: Elimina todos los elementos de la lista
x = [2, 3, 4]
x.clear()
print("Lista después de clear():", x)  # Salida: []

x = [2, 3, 4]
y = x.clear()  # clear() modifica la lista en su lugar y devuelve None
print("Resultado de y tras clear():", y)  # Salida: None

x = [2, 3, 4]
y = x  # Asignamos la misma referencia
x.clear()
print("Lista y después de limpiar x:", y)  # Ambas referencias apuntan a la lista vacía

# Método copy: Crea una copia independiente de la lista
x = [2, 3, 4]
y = x.copy()
print("Lista x:", x)
print("ID de x:", id(x))
print("Lista copiada y:", y)
print("ID de y:", id(y))  # La copia tiene una dirección diferente en memoria

# Método append: Agrega un elemento al final de la lista
x = [2, 3, 4]
x.append(7)
print("Lista después de append(7):", x)  # Salida: [2, 3, 4, 7]

# Método insert: Inserta un elemento en una posición específica
x = [2, 3, 4]
x.insert(1, 8)  # Insertamos 8 en la posición 1
print("Lista después de insert(1, 8):", x)  # Salida: [2, 8, 3, 4]

# Método pop: Elimina y devuelve el último elemento de la lista
x = [2, 3, 4]
x.pop()
print("Lista después de pop():", x)  # Salida: [2, 3]

# pop con retorno de valor
x = [2, 3, 4]
y = x.pop()  # Se elimina el último elemento y se guarda en 'y'
print("Elemento eliminado con pop():", y)  # Salida: 4

# pop con índice específico
x = [2, 3, 4]
y = x.pop(1)  # Se elimina el elemento en la posición 1
print("Lista después de pop(1):", x)  # Salida: [2, 4]
print("Elemento eliminado con pop(1):", y)  # Salida: 3