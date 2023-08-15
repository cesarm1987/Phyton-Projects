#practica 3

#Solicitamos datos al usuario
name = input("Ingrese su nombre: ")
print(f"Hola, {name}. Bienvenido a la calculadora de descuentos de")
print("la tienda de repuestos CJM")
print("\nIngrese el numero del elemento que desea comprar. \n")
print("1- Repuestos para el motor           15% OFF\n")
print("2- Repuestos accesorios              10% OFF\n")
print("3- Repuestos para limpieza del auto   5% OFF\n")
print("4- Repuestos para los frenos          3% OFF\n")
x=int(input())
precio=int(input("Ingrese el precio del producto: "))
cant=int(input("Ingrese la cantidad de articulos que compro: "))
print("\n\n\n")

#Empezamos a desarrollar las operaciones
if x==1:
    total=(precio*cant)-(precio*cant*0.15)
    articulo="Repuestos para el motor"
    descuento=0.15
if x==2:
    total=(precio*cant)-(precio*cant*0.10)
    articulo="Repuestos accesorios"
    descuento=0.10
if x==3:
    total=(precio*cant)-(precio*cant*0.05)
    articulo="Repuestos para la limpieza del auto"
    descuento=0.05
if x==4:
    total=(precio*cant)-(precio*cant*0.03)
    articulo="Repuestos para los frenos"
    descuento=0.03

#Se imprimen las salidas y los resultados
print("\n\n\n              Factura\n")
print(f"Cliente: {name}")
print(f"Producto: {articulo}")        
print(f"Cantidad:                            {cant}")
print(f"Precio:                              ${precio*cant}")
print(f"Descuento {descuento*100}%                      -${precio*cant*descuento}")
print(f"Total a pagar:                       ${total}")
print(f"\nGracias por su compra, {name}!")
