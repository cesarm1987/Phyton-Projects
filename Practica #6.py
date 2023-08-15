#Practica

# Declaracion de las variables

nombres={}
notas={}

# Empezamos agregando los vectores o arrays
# los calculos y las operaciones se realizan en esta etapa

for x in range(0,10):
    nombres[x]=input("Digite el nombre: ")
    notas[x]=int(input("Digite la nota: "))

def despliegue():
    for x in range(0,10):
        print(nombres[x],"  ",notas[x])

def sumar3():
    for x in range(0,10):
        if notas[x] >= 98:
            notas[x] = 100
        else:
            notas[x]=notas[x]+3

def altabaja():
    alta=0

    for x in range(0,10):
        if notas[x]>alta:

            alta=notas[x]
    baja=alta

    for x in range(0,10):
        if notas[x]<baja:
            baja=notas[x]

# Imprimimos el mensaje de las notas tanto la mas alta como la mas baja

    print("La nota mas alta es: ",alta," la nota mas baja es: ",baja)

def aprobaron():
    reprobados=0

    for x in range(0,10):
        if notas[x] < 70:
            reprobados=reprobados+1

# Validamos cuales estudiantes reprobaron el curso e imprimos un mensaje con los que perdieron la materia

    print(reprobados," perdieron la materia")

# Agregamos algunas variables que nos ayudan en el calculo de las operaciones

sumar3()
despliegue()
altabaja()
aprobaron()