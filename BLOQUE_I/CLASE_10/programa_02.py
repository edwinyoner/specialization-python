
#CANTIDAD INDETERMINADA
#Por posición/orden
def suma(*args):
    return args

r1 = suma(1, 2, 3, 4)
print(r1)

def sumaDeNumeros(*args):
    suma = 0
    for i in args:
        suma += i

    return suma

print("Suma de los n números es:", sumaDeNumeros(1, 2, 3))

def factorial(valor):
    fact = 1
    for i in range(1, valor+1):
        fact *= i
    return fact

print("El factorial de ", 5, " es: ", factorial(5))

#Por nombre
def suma(**kwargs):
    return kwargs

r = suma(a=1, b=2, c=3, d=4)
print(r)

def suma(**kwargs):
    total = 0
    for valor in kwargs.values():
        total += valor
    return total

r = suma(a=1, b=2, c=3, d=4)
print("La suma es:", r)

def suma (**kwargs):
    s=0
    for i in kwargs:
        s = s+kwargs[i]
        return s
r1= suma(a=1, b=2,c=3,d=4)
print(r1)

a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for i in a:
    print(i, a[i])

#Combinación
def suma(*args, **kwargs):
    total1 = 0
    for i in kwargs:
        total1 += kwargs[i]

    total2 = 0
    for i in args:
        total2 += i
    return total1 + total2

r = suma(3, 4, 3, a = 1, b = 2, c = 3, d = 4)
print("La suma es total es:", r)

def suma(x, y, *args, w=0, z=1, **kwargs):
    return x+y+z

r1 = suma(1,2,3,4,6)
print(r1)

r1 = suma(1,2,3,z=2)
print(r1)

r1 = suma(1,2,3,a=2,b=3)
print(r1)

def suma(*args,w=0,z=1, **kwargs):
    return kwargs
r1=suma(1,2,3,4,6)
r2 =suma(1,2,3,z = 2)
r3=suma(1,2,3,a = 2)