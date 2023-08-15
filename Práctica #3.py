#Imprime mensajes de encabezado del programa

print("\t*****Repuestos La Mejor Opción*****")
print()
print('''          Tipo                      Descuento 
         1. Repuestos para el motor 	        15%
         2. Repuestos accesorios 	        10%
         3. Repuestos para limpieza del auto     5%
         4. Repuestos para los frenos 	         3%

         ''')


#Solicita los datos al usuario

nombre= input("Ingrese su nombre completo: ")
opcion= input("Ingrese el número de opción del tipo de repuesto que va comprar: ")
cantidad = int(input("Ingrese la cantidad de repuestos del tipo escogido que va comprar: "))
precio = float(input("Ingrese el precio unitario del repuesto escogido: "))

#Filtra la opción y aplica las operaciones

if opcion == "1":
    producto = "Repuestos para el motor"
    subtotal = cantidad * precio
    descuento = subtotal *0.15
elif opcion == "2":
    producto = "Repuestos accesorios"
    subtotal = cantidad * precio
    descuento = subtotal *0.1
elif opcion == "3":
    producto = "Repuestos limpieza de auto"
    subtotal = cantidad * precio
    descuento = subtotal *0.05
elif opcion == "4":
    producto = "Repuestos para los frenos"
    subtotal = cantidad * precio
    descuento = subtotal *0.03
else:
    print("El tipo de repuesto escogido no está entre las opciones válidas")


#Despliega la información tipo factura
print()
print("\t*****Repuestos La Mejor Opción*****")
print("FACTURA DE CONTADO")
print("Nombre del cliente: ",nombre)
print()
print("Producto:            ",producto)
print("Cantidad:            ",cantidad)
print("Precio unitario:     ",precio)
print("Subtotal:            ",subtotal)
print("Descuento:           ",descuento)
print("Precio final:        ", subtotal-descuento)
print()
print("****Gracias por comprar en nuestra empresa***")


