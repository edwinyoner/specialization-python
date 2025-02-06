#04/02/2025
#CANNTIDAD DETERMINADA
#Por posición/orden
def suma(x, y):
    c = x + y
    return c

print(suma(2, 3))

#Por nombre
def suma(x, y):
    c = x + y
    print("x", x)
    print("y", y)
    return c

print(suma(y = 2, x = 3))

#Por valores por default en parámetro
def suma(x=0, y=0):
    c = x + y
    print("x", x)
    print("y", y)
    return c

print(suma(y=4))

#Combinar
def suma(x,y, z =0, w=5):
    c = x + y -z-w
    return c

print(suma(2, 3))
print(suma(1, 2, 6, 8))
print(suma(1, 2, w = 0))
print(suma(x=1, y=2, w=6))

