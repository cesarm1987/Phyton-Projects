# Declarar matriz, indices y variable

matriz = [["",0,0],["",0,0],["",0,0],["",0,0],["",0,0]]
x = 0
y = 0
opcion = 0

# Agregar los procesos

def Menu():


    opcion = int(input("Bienvenido! "
                       "\n1. Registro de Prodcutos.  "
                       "\n2. Consulta de Producto.  "
                       "\n3. Modificar Producto. "
                       "\n4. Salir. "
                       "\n Seleccione una opcion:"))


    if opcion == 1:
        Producto()
        Cantidad()
        Precio()
        Imprimir()
    elif opcion == 2:
      Consulta()
    elif opcion ==3:
        Modificar()
    elif opcion == 4:
       exit()

def Producto():
    for x in range(0,5):
     for y in range(0,1):
         matriz[x][0]= input("Ingrese el nombre del producto:")

def Cantidad():
    for x in range(0,5):
        for y in range(0,1):
            matriz[x][1] = int(input("Ingrese la cantidad que desea:"))

def Precio():
    for x in range(0,5):
        for y in range(0,1):
            matriz[x][2] = int(input("Ingrese el precio:"))

def Consulta():

    dato = int(input("1.Nombre,cantidad de unidades. "
                   "\n2.Precio del producto por unidad."
                    "\nQue desea consultar:"))

    if dato == 1:
        n= input("Ingrese el nombre del producto que desea consultar:")
        for x in range(0,5):
            for y in range(0,1):
                if matriz[x][0]== n:
                    print("El producto consultado es:" ,matriz[x][0],
                        "\nUnidades disponibles:"      ,matriz[x][1],"uds" )
    elif dato == 2:
        n= input("Ingrese el nombre del producto que desea consultar:")
        for x in range(0,5):
            for y in range(0,1):
                if matriz[x][0]== n:
                    print("El producto consultado es:",matriz[x][0],
                          "\nUnidades disponibles:"     ,matriz[x][1],"uds",
                          "\nPrecio por unidad:"        ,"$",matriz[x][2])
    else:
        exit("Valor invalido")

def Modificar():

    productoActual = input("Cual producto desea cambiar:")
    nuevoProducto = input("Ingrese el producto nuevo:")
    for x in range(0,5):
        for y in range(0,3):
          if matriz[x][y] == productoActual:
              matriz[x][y]=nuevoProducto
              print("Su producto ha sido ingresado exitosamente")

def Ejecucion():

    while opcion != 4:
        Menu()

def Imprimir():
    for x in range(0,5):
        for y in range(0,3):
            print(matriz[x][y],end=" ")
        print("\n")

# Imprimir resultados

Ejecucion()
Menu()
Imprimir()