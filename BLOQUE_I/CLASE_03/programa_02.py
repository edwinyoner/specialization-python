"""
Archivo: programa_02.py
Autor: Edwin Yoner
Fecha: 18/01/2025

Descripción:
    Este programa explora el comportamiento de las listas en Python,
    incluyendo cómo las referencias a variables afectan la mutabilidad de los datos.
"""

# Definimos una variable y una lista que la contiene
a = 2
x = [a, 8, 4]

# Modificamos el primer elemento de la lista
x[0] = 6

# Imprimimos la lista modificada
print("Lista x después de la modificación:", x)

# Imprimimos el valor de 'a' para verificar si ha cambiado
print("Valor de a:", a)  # 'a' sigue siendo 2, ya que en listas solo se almacena la referencia inicial, no la variable en sí

# Definimos dos listas separadas
x = [2, 3, 4]
y = [3, 8]

# Imprimimos la identidad de los elementos en la memoria
print("ID de x[1]:", id(x[1]))  # Muestra la dirección en memoria del número 3 en la lista x
print("ID de y[0]:", id(y[0]))  # Muestra la dirección en memoria del número 3 en la lista y

# En Python, los valores inmutables (como enteros) con el mismo contenido pueden compartir la misma dirección en memoria,
# por lo que los ID de `x[1]` y `y[0]` podrían ser iguales.