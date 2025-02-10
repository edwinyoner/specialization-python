def suma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + suma_recursiva(lista[1:])

s = [2, 3, 4, 1, 0, 5]
resultado = suma_recursiva(s)
print(f"La suma de los elementos de la lista es: {resultado}")
