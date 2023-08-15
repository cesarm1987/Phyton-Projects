print("1)Calcular Area de un circulo: ")
print("")
print("2)Calcular Area de un cuadrado ")
print("")
print("3 Calcular Area de un triangulo rectangulo ")
print("")
print("Ingrese la opcion: ")
opcion = int(input())

if opcion == 1:
    print("Ingrese el radio del circulo: ")
    radio = int(input())
    area = 3.1415 * (radio * radio)
    print("El Area del circulo es: ", area)

elif opcion == 2:
        print("Ingrese la longitud del lado del cuadrado: ")
        lado = int(input())
        area = lado * lado
        print("El Area del cuadrado es: ", area)

elif opcion == 3:
        print("Ingrese la longitud de la base: ")
        base = int(input())
        print("Ingrese la longitud de la altura: ")
        altura = int(input())
        area = (base*altura) /2
        print("El Area del triangulo rectangulo es: ", area)
