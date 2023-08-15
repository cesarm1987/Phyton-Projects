# Imprime mensajes de encabezado del programa

print("\t*****Bienviendo a La Ferreteria Moreira*****")
print()
print('''   Productos                       
         1. Martillos 	        
         2. Serruchos 	        
         3. Sistemas de enfriamiento     
         4. Limpiador de aceleracion  	         

         ''')

# Validamos los datos con el cliente

nombre= input("Ingrese su nombre completo: ")
opcion= int(input("Ingrese el producto que desea comprar: "))
precio = float(input("Ingrese el precio unitario del articulo: "))
cantidad = int(input("Ingrese la cantidad de unidades que desea comprar: "))

# Agregamos las clases en funcion de los productos
class sistema:
  if  opcion == 1:
    producto = "Martillo"
    subtotal = cantidad * precio
  elif opcion == 2:
    producto = "Serruchos"
    subtotal = cantidad * precio
  elif opcion == 3:
    producto = "Sistemas de enfriamiento"
    subtotal = cantidad * precio
  elif opcion == 4:
    producto = "Limpiador de aceleracion"
    subtotal = cantidad * precio
  else:
    print("El tipo de repuesto escogido no está entre las opciones válidas")

pass;

class descuento:

   if cantidad <= 10:
       des = sistema.subtotal* 0.05
   elif cantidad > 10 or cantidad < 20:
       des = sistema.subtotal * 0.10
   elif cantidad >= 20:
       des = sistema.subtotal * 0.15
   else:
       print("No aplica el descuento")

pass;

# Realizamos las operaciones matématicas

iva = round(sistema.subtotal * 0.13)
total = sistema.subtotal + iva
preciofinal = total-descuento.des

# Despliegamos la información de la factura

print()
print("\t*****Ferreteria Moreira*****")
print("FACTURA DE CONTADO")
print("Nombre del cliente: ",nombre)
print()
print("Producto:            ",sistema.producto)
print("Cantidad:            ",cantidad)
print("Precio unitario:     ",precio)
print("Subtotal:            ",sistema.subtotal)
print("IVA:                 ",iva)
print("Descuento:           ",descuento.des)
print("Total a pagar:       ",preciofinal)


print()
print("****Gracias por su compra***")


