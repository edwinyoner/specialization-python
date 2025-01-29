nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))

promedio = (nota1 + nota2) / 2

if promedio >= 11:
    print("Aprobado con promedio: ", promedio)
else:
    print("Desaprobado con promedio: ", promedio)