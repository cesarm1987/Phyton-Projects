#Practica 5
#
#Variables
#TipoNeumatico
#Cantidad
#CostoTotal

TipoNeumatico = 0
Cantidad = 0
s = ""
CostoTotal = 0.00
Descuento = 0.00
MontoDescuento = 0.00
IVA = 0.00
Seleccion = 0


def calculo():
    global CostoTotal
    global Descuento
    if TipoNeumatico == 1:
        if Cantidad > 10:
            print("primera opcion")
            print("El costo total es: ",12000*Cantidad)
            print("Le corresponde un 5% de descuento")

            CostoTotal=12000*Cantidad
            Descuento=0.05

        else:
            print("El costo total es: ",12000*Cantidad)
            print("Le corresponde un 0% de descuento")
            #global CostoTotal
            CostoTotal=12000*Cantidad
            #global Descuento
            Descuento=1

    elif TipoNeumatico == 3:
        if Cantidad > 10:
            print("segunda opcion")
            print("El costo total es: ",45000*Cantidad)
            print("Le corresponde un 10% de descuento")

            CostoTotal=45000*Cantidad

            Descuento=0.10

        else:
            print("El costo total es: ",45000*Cantidad)
            print("Le corresponde un 0% de descuento")

            CostoTotal=45000*Cantidad

            Descuento=1

    elif TipoNeumatico == 2:
        if Cantidad > 10:
            print("tercera opcion")
            print("El costo total es: ",25000*Cantidad)
            print("Le corresponde un 7% de descuento")

            CostoTotal=25000*Cantidad

            Descuento=0.07
        else:
            print("El costo total es: ",25000*Cantidad)
            print("Le corresponde un 0% de descuento")

            CostoTotal=25000*Cantidad

            Descuento=1
    else:
        print("lo que sigue")

def descuento():
    print("El costo total es: ",CostoTotal," y el monto de escuento es: ",CostoTotal*Descuento)

def calculoiva():
    global IVA
    IVA=(CostoTotal-Descuento)*0.13
    print("El IVA corresponde a: ",IVA)

def factura():
    print("Facturacion Venta de Neumaticos")
    if TipoNeumatico == 1:
        print("Escogio",Cantidad," neumaticos sinteticos")
    elif TipoNeumatico == 2:
        print("Escogio",Cantidad," neumaticos naturales")
    elif TipoNeumatico == 3:
        print("Escogio",Cantidad," neumaticos hibridos")
    print("El costo total es de :",CostoTotal)
    print("El descuento aplicado es :",CostoTotal*Descuento)
    print("El IVA es :",IVA)
    print("El monto a pagar es:",(CostoTotal-(CostoTotal*Descuento)+(CostoTotal-Descuento)*0.13))

#calculo()
#descuento()
#calculoiva()
#factura()
while s != "s":
    pass


    print("\t\t\tVenta de Neumaticos")
    print("Los precios de los neumaticos son:")
    print("1-Sinteticos: 12000")
    print("2-Naturales: 25000")
    print("3-Hibridos: 45000")
    TipoNeumatico = int(input("Digite el tipo de neumatico que desea: "))
    Cantidad = int(input("Digite la cantidad de neumaticos por comprar: "))
    print("4-Calculo de precio")
    print("5-Calculo del descuento")
    print("6-Calculo IVA")
    print("7-Facturacion")
    print("8-Salir")
    #s = input("Desea salir ? s/n :")
    Seleccion = int(input("Favor escoga una opcion : "))
    if Seleccion == 4:
        calculo()
    elif Seleccion == 5:
        descuento()
    elif Seleccion == 6:
        calculoiva()
    elif Seleccion == 7:
        factura()
    elif Seleccion == 8:
        break