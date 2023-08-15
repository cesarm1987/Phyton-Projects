cliente= []
opcion = 0
x=0



def inclusionFactura():
   opc = 0
   vendido = 0
   desfint = ''
   for i in range(7):
    nombre= input("Ingrese su nombre:")
    cliente.append(nombre)
    fecha = input("Ingrese la fecha que realizo la compra:")
    cliente.append(fecha)
    cantidad = int(input("Ingrese la cantidad de litros comprados: "))
    cliente.append(cantidad)
    opc= int(input("\n1.Regular"
                   "\n2.Industrial"
                   "\nIngrese el tipo de desinfectante que desea:"))
    if opc == 1:
           desfint = 'Regular'
           vendido = 300 * int(cantidad)
    elif opc == 2:
           desfint = 'Industrial'
           vendido = 250 * int(cantidad)
    cliente.append(desfint)
    cliente.append(vendido)
    aroma = input("Ingrese el aroma que desea:")
    cliente.append(aroma)
    if cantidad >= 10:
        desc = vendido * 0.1
    else:
        desc = 0
    cliente.append(desc)
    iva= (vendido - desc)* 0.13
    cliente.append(iva)
    total = vendido - desc + iva
    cliente.append(total)
    return(cliente)



def despliegueFactura():
    print("Desinfectantes Morera","\nNumero Tel:84289319")
    print("\nCliente:      ",cliente[0],
          "\nFecha:        ",cliente[1],
          "\nCantidad:      ",cliente[2],
          "\nDesinfectante: ",cliente[3],
          "\nTotal:          ",cliente[4],
          "\nAroma:          ",cliente[5],
          "\nDescuento:      ",cliente[6],
          "\nIVA:            ", cliente[7],
          "\nPrecio final:   ", cliente[8],)
    return(cliente[x])

def guardarArchivo():
    despliegueFactura()
    file = open("Factura Desinfectante Morera.txt", "w")
    print("El archivo ha sido creado exitosamente")

    file.write('Cliente=%s'%str(cliente[0]))
    file.write("\n")
    file.write('Fecha=%s'%str(cliente[1]))
    file.write("\n")
    file.write('Cantidad=%s'%str(cliente[2]))
    file.write("\n")
    file.write('Desinfectante=%s'%str(cliente[3]))
    file.write("\n")
    file.write('Total=%s'%str(cliente[4]))
    file.write("\n")
    file.write('Aroma=%s'%str(cliente[5]))
    file.write("\n")
    file.write('Descuento=%s'%str(cliente[6]))
    file.write("\n")
    file.write('IVA=%s'%str(cliente[7]))
    file.write("\n")
    file.write('Precio Final=%s'%str(cliente[8]))
    file.write("\n")
    file.close()

def Imprimir():
    file = open("Factura Desinfectante Morera.txt","r")
    mensaje = file.read()
    print(mensaje)
    file.close()
def Menu():

    opcion = int(input("Bienvenido! "
                       "\n1. Ingresar datos.  "
                       "\n2. Despliegue de factura.  "
                       "\n3. Guardar Archivo. "
                       "\n4. Imprimir Archivo. "
                       "\n5. Salir."
                       "\n Seleccione una opcion:"))

    if opcion == 1:
        inclusionFactura()
    elif opcion == 2:
        despliegueFactura()
    elif opcion == 3:
        guardarArchivo()
    elif opcion == 4:
        Imprimir()
    elif opcion == 5:
       exit()

def Ejecucion():

    while opcion != 5:
        Menu()



Ejecucion()