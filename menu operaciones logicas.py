#Procedimientos

def sumar(x,y):
    resultado = x + y
    return resultado

def restar(x,y):
    return x - y

def multiplicar(x,y):
    resultado = x * y
    return resultado

def dividir(x,y):
    resultado = x / y
    return resultado

def menu():
##Funcion que limpia la pantalla y muestra nuevamente el menu
    print ("Selecciona una opcion")
    print ("\t1 - Suma")
    print ("\t2 - Resta")
    print ("\t3 - Multiplicacion")
    print ("\t4 - Division")
    print ("\t9 - Salir")

#Programa principal
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))

while True:
    # Mostramos el menu
    menu()

    # solicitamos una opcion al usuario
    print()
    opcionMenu = input("Ingrese la opcion de la operacion: ")

    if opcionMenu=="1":
        resultado = sumar(a,b)
        print("La suma es ", resultado)
    elif opcionMenu=="2":
        print("La resta es ", restar(a,b))
    elif opcionMenu=="3":
        print("La multiplicacion es: ", multiplicar(a,b))
    elif opcionMenu=="4":
        print("La division es: ", dividir(a,b))
    elif opcionMenu=="9":
        break
    else:

        print("")
        input("No has pulsado ninguna opcion...\npulsa una tecla para continuar")


    print ("\n***Gracias por utilizar nuestro programa***")

















        
