# Declarar matriz e indices

matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x=0
y=0

# Agregar los procesos

def llenadomatriz():

    for x in range (0,5):
        for y in range (0,5):
            matriz[x][y]=int(input("Favor digite un numero: "))

def sumafila():

    fila0=0
    fila1=0
    fila2=0
    fila3=0
    fila4=0

    for x in range (0,5):
        for y in range (0,5):
            if x==0:
                fila0=fila0+matriz[x][y]
            elif x==1:
                fila1=fila1+matriz[x][y]
            elif x==2:
                fila2=fila2+matriz[x][y]
            elif x==3:
                fila3=fila3+matriz[x][y]
            elif x==4:
                fila4=fila4+matriz[x][y]
    print("Fila1=",fila0)
    print("Fila2=",fila1)
    print("Fila3=",fila2)
    print("Fila4=",fila3)
    print("Fila5=",fila4)


def promedio():
    promedio=0.00
    for x in range(0,5):
        for y in range(0,5):
            promedio=promedio+matriz[x][y]
    promedio=promedio/25
    print("El valor promedio es: ",promedio)


def par():
    pares=0
    for x in range(0,5):
        for y in range(0,5):
            if (matriz[x][y] % 2) == 0:
                pares=pares+1
    print("Hay ",pares," numeros pares")

def Imprimir():
    print("La matriz original es: ")
    print(matriz, end=" ")
    print("\n")

def filax2():

    for x in range (0,5):
        for y in range(0,5):

            if x==2:

                matriz[x][y]=matriz[x][y]*2


    print("La matriz multiplicada por 2 la tercera fila es: ")
    print(matriz, end=" ")
    print("\n")

# Imprimir los resultados

llenadomatriz()
sumafila()
promedio()
par()
Imprimir()
filax2()