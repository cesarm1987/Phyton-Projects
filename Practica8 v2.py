import os

def agregar():
    for i in range(20):
        datos[i]=input("Digite el nombre que desea incluir: ")

    file = open("Nombres.txt","w")
    for i in range(20):
        file.write (datos[i] + "\n")
    file.close()

def consulta():
    file = open("Nombres.txt","r")
    archivo = file.read()
    otros = archivo.split("\n")
    nombre=""
    nombre=input("Digite el nombre que desea consultar: ")
    existe=0
    for x in range(20):
        if nombre==otros[x]:
            existe=1
            posicion=x

    if existe==1:
        print("El empleado :",nombre," si existe")
    if existe==0:
        print("El empleado :",nombre," no existe")
    file.close()

def modificar():
    file = open("Nombres.txt","r")
    archivo = file.read()
    otros = archivo.split("\n")
    file.close()

    pormodificar=""
    existe=0


    pormodificar=input("Digite el dato a modificar :")
    for x in range(20):
        if pormodificar==otros[x]:
            existe=1
            posicion=x
    if existe==1:
        print("Nombre encontrado")
        nuevonombre=input("Digite el nuevo nombre: ")
        print(otros[posicion], " ha sido cambiado por ",nuevonombre)
        otros[posicion]=nuevonombre

    if existe==0:
        print("Nombre no encontrado")

    file = open("Nombres.txt","w")
    for dato in otros:
        file.write (dato + "\n")
    file.close()

def eliminar():
    poreliminar=""
    existe=0
    x=0
    file = open("Nombres.txt","r")
    nombres=file.read()
    otros=nombres.split("\n")
    file.close()

    poreliminar=input("Digite el nombre a eliminar: ")
    for x in range(20):
        if poreliminar == otros[x]:
            existe=1
            posicion=x

    if existe==1:
        print("Nombre encontrado")
        otros.pop(posicion)
        print("El nombre ",poreliminar," ha sido eliminado")

    if existe==0:
        print("Nombre ingresado no existe")

    file = open("Nombres.txt","w")
    for dato in otros:
        file.write (dato +"\n")

    file.close()

def imprimir():
    file = open("Nombres.txt","r")
    archivo = file.read()
    otros = archivo.split("\n")
    for i in otros:
        print(i)
    file.close()


def menu():

    while True:
        opcion=0
        print("*****Menu Principal*****")
        print("1-Ingresar empleado")
        print("2-Consultar empleado")
        print("3-Modificar empleado")
        print("4-Eliminar empleado")
        print("5-Imprimir empleados")
        print("6-Salir")

        opcion=int(input("Digite la opcion seleccionada: "))

        if opcion==1:
            agregar()
        elif opcion==2:
            consulta()
        elif opcion==3:
            modificar()
        elif opcion==4:
            eliminar()
        elif opcion==5:
            imprimir()
        elif opcion==6:
            break
        else:
            print("Favor seleccione una opcion valida")

datos=["","","","","","","","","","","","","","","","","","","",""]


menu()


def posicion():
    pass


posicion()