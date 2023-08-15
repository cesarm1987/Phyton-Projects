import random
import os


def menu():  # Se crea en un subprograma para escribir el menú
    sumaTotal = 0
    while True:
        opcion = ""
        print("********************************************************")
        print()
        print("\t   ****MENÚ PRINCIPAL****  \t")
        print("\t   ****EJERCICIO 1****  \t")
        print()
        print("\t1 - Sumar matriz")
        print("\t2 - Promedio")
        print("\t3 - Eleva al cuadrado")
        print("\t4 - Regraba el archivo plano")
        print("\t5 - Salir")
        print()
        print()
        print("********************************************************")
        print()
        opcion = input("Ingrese la opción deseada: ")

        # Con los if anidados se llama a los subprogramas de cada opción

        if opcion == "1":
            sumaTotal = suma_matriz()
            print()
        elif opcion == "2":
            promedio(sumaTotal)
            print()
        elif opcion == "3":
            eleva_cuadrado()
            print()
        elif opcion == "4":
            regrabar()
            print()
        elif opcion == "5":
            break
        else:
            print()
            input("ERROR: Carácter inválido...\nPulse una tecla para continuar")


def suma_matriz():
    totalSuma = 0

    print("La matriz a sumar es la siguiente:\n")
    imprimir()
    for i in range(5):
        suma = 0
        for k in range(5):
            suma += numeros[i][k]
            totalSuma += numeros[i][k]
        print("\nLa suma de la fila", i + 1, "es:", suma)
    return totalSuma


def promedio(totalSuma):
    if totalSuma == 0:
        print("Aún no se ha sumado la matriz, vuelva al menú y súmela primero")
    else:
        prom = totalSuma / 25
        print("\nEl promedio corresponde a", prom)
        print("La suma de todos los elementos corresponde a", totalSuma, "\n")


def eleva_cuadrado():
    print("\nMatriz original\n")
    imprimir()
    for i in range(5):
        for k in range(5):
            numeros[i][k] = numeros[i][k] ** 2
    print("\nMatriz elevada al cuadrado\n")
    imprimir()


def regrabar():
    file = open("numeros.txt", "w")
    for i in range(5):
        for j in range(5):
            file.write(str(numeros[i][j]) + " ")
    file.close()
    print("\nEl archivo ha sido regrabado\n")


def imprimir():
    for i in range(5):
        for j in range(5):
            print(numeros[i][j], end=" ")
        print()


# Principal
numeros = []

for i in range(5):
    numeros.append([0] * 5)

for i in range(5):
    for k in range(5):
        numeros[i][k] = int(random.randrange(1, 50))

file = open("numeros.txt", "w")
for i in range(5):
    for j in range(5):
        file.write(str(numeros[i][j]) + " ")

file.close()

menu()
print("Muchas gracias por utilizar nuestro programa")