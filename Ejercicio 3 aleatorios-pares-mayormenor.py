#Ejercicio 3
'''Crear un programa que llene un vector con números
aleatorios de 50 a 100 y despliegue el vector, cantidad
de números pares y los números mayor y menor del arreglo.
#Inclusión de la librería RANDOM'''

import random
#Subprogramas

def pares(arreglo):
    suma = 0
    for x in arreglo:
        if x%2 == 0:
            suma += 1
    
    print("La cantidad de números pares es: ", suma)
    print()
    
def mayor_menor(arreglo):
    
    mayor = arreglo[0]
    menor = arreglo[0]
    for x in arreglo:
        if x > mayor:
            mayor = x
    for x in arreglo:
        if x < menor:
            menor = x
    print("El número mayor es: ", mayor)
    print("El número menor es: ", menor)
    print()

#Solicitud de información
numeros =[]

#incluye 10 números aleatorios del 50 al 100
for x in range(10):
    numeros.append(int(random.randrange(50,100)))#Se llena el arreglo con números aleatorios del 50 al 99

print("Los números ingresados son:")
print(numeros)
print()
pares(numeros)
mayor_menor(numeros)
