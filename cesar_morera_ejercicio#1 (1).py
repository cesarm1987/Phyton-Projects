# Parcial Test 1.

# Declaramos las variables con las que vamos a trabajar

Basico = 90000;
Medio = 150000;
Premium = 200000;
VIP = 250000;
X = 0;
interes = float;
Y = 0
porcentaje = float;


print("Bienvenido a la Floreria Rojas")

# Agregamos cada una de las clases en relacion a los paquetes

class paquete:
    X = int(input("Contamos con los siguientes paquetes:  \n1.Basico   \n2.Medio  \n3.Premium  \n4.VIP  \nPor favor haga su eleccion: " ))
    if X == 1:
        X = Basico
        Msg = "El paquete que se ha seleccionado es el Basico"
    elif X == 2:
        X = Medio
        Msg = "El paquete que se ha seleccionado es el Medio"
    elif X == 3:
        X = Premium
        Msg = "El paquete que se ha seleccionado es el Premium"
    elif X == 4:
        X = VIP
        Msg = "El paquete que se ha seleccionado es el VIP"
    else:
        print("El paquete seleccionado es incorrecto")
        exit()
        pass;

pass;

# Agregamos las clases en relacion a las cuotas que se van a pagar

class intereses:
    Y = int(input("Las cuotas con las que contamos en este momento para realizar los pagos son las siguiente:  \nOpcion 2 cuotas 6%. \nOpcion 4 cuotas 12%. \nOpcion 8 cuotas 16%.  \nElija la cuota que desea: "))
    if Y == 2:
        interes = 0.06
        porcentaje = 0.06 * 100
    pass;
    if Y == 4:
        interes = 0.12
        porcentaje = 0.12 * 100
    pass;
    if Y == 8:
        interes = 0.16
        porcentaje = 0.16 * 100
    pass;


pass;

# Realizamos las operaciones matématicas

cuota = float((paquete.X * intereses.interes) + paquete.X) / intereses.Y
recargo = int(paquete.X * intereses.interes)

# Imprimimos los resultados del programa en pantalla

print(".................................")
print(paquete.Msg)
print("Monto del paquete es:",paquete.X)
print("Cantidad de cuotas por pagar:",intereses.Y)
print("Recargo de acuerdo con las cuotas:",recargo)
print("Interes porcentual:",intereses.porcentaje, "%")
print("Cuota por pagar:",cuota)
print(".................................")
print("Gracias por usar nuestro sistema. Lo esperamos pronto!")

    
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
