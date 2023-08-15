#Datos del usuario
print("\t\t\t\t\t")
print("\t\t\t\t¡¡COMPRA POR TRIOS!!")
print("\t\t\t\t\t")
Prod1 = str(input("Ingrese el primer producto: "))
Precio1 = int(input("Ingrese el precio del producto: "))
Cant1 = int(input("Ingrese cantidad de producto: "))
Prod2 = str(input("Ingrese el segundo producto: "))
Precio2 = int(input("Ingrese el precio del producto: "))
Cant2 = int(input("Ingrese cantidad de producto: "))
Prod3 = str(input("Ingrese el tercer producto: "))
Precio3 = int(input("Ingrese el precio del producto: "))
Cant3 = int(input("Ingrese cantidad de producto: "))
#Realiza operaciones

total = Cant1 * Precio1
total2 = Cant2 * Precio2
total3 = Cant3 * Precio3
total4 = total + total2 + total3
desc = total4 * 0.10
iva = (total4 - desc) * 0.13
final = (total4 - desc) + iva

#imprime el mensaje
print("--------------------------------------------------------------------------------------------")
print("\t\t\t\t\tFactura")
print("Producto \t\t Cantidad \t\t Precio \t\t Subtotal")
print(Prod1,"\t\t\t", Cant1,"\t\t\t", Precio1,"\t\t\t", total)
print(Prod2,"\t\t", Cant2,"\t\t\t", Precio2,"\t\t\t", total2)
print(Prod3,"\t\t", Cant3,"\t\t\t", Precio3,"\t\t\t", total3)
print("Subtotal\t\t\t\t\t\t\t\t", total4)
print("Descuento 10%\t\t\t\t\t\t\t\t", desc)
print("IVA 13%\t\t\t\t\t\t\t\t\t", iva)
print("\t")
print("Total\t\t\t\t\t\t\t\t\t", final)
print("Su ahorro fue de\t\t\t\t\t ", desc)
print("--------------------------------------------------------------------------------------------")
