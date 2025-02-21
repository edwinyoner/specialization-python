"""
Archivo: programa_01.py
Autor: Edwin Yoner
Fecha: 15/02/2025

Descripción:
    Este programa solicita al usuario ingresar un número y realiza la operación 5 / x.
    Se implementa manejo de excepciones para evitar errores comunes como entrada inválida,
    división por cero y cierre inesperado del programa.
"""

while True:
    try:
        # Solicitar al usuario un número
        numero = float(input("Ingrese un número: "))

        # Realizar la operación
        resultado = 5 / numero
        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: Solo está permitido ingresar números.")

    except TypeError:
        print("Error: Se produjo un problema con el tipo de dato ingresado.")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0. Intente con otro número.")

    except KeyboardInterrupt:
        print("\nInterrupción detectada. Finalizando el programa...")
        break  # Sale del bucle cuando el usuario presiona Ctrl + C

    except Exception as e:  # Captura cualquier otro error no previsto
        print(f"Se ha producido un error inesperado: {e}")

    finally:
        print("Operación finalizada. Intente nuevamente.\n")
