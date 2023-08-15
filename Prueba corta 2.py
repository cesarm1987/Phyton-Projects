#Creación de variables

pesoGallina = 0
alturaGallina = 0
cantidadHuevos = 0

#Muestra el menú

print("----- Bienvenido -----")

print("----------------------------------------------")
print("|            1. Calculo de precio            |")
print("|            2. Salir                        |")
print("----------------------------------------------")

menu = int(input("Ingrese la opción del menú: "))

print()
print()

#Realiza las operaciones y filtros

while menu == 1:

    pesoGallina = int(input("Ingrese el peso de la gallina(Kilos): "))
    alturaGallina = int(input("Ingrese la altura de la gallina(cm): "))
    cantidadHuevos = int(input("Ingrese la cantidad de huevos que pone la gallina: "))

    calidadGallina = pesoGallina*alturaGallina/cantidadHuevos

    if calidadGallina <= 8:
        precio = (0.80*calidadGallina)
        print("El promedio de calidad de la gallina es:", calidadGallina)
        print("El precio por kilo de los huevos es: ₵", precio)
    elif calidadGallina > 8 and calidadGallina < 15:
        precio = (1.00*calidadGallina)
        print("El promedio de calidad de la gallina es:", calidadGallina)
        print("El precio por kilo de los huevos es: ₵", precio)
    elif calidadGallina >= 15:
        precio = (1.2*calidadGallina)
        print("El promedio de calidad de la gallina es:", calidadGallina)
        print("El precio por kilo de los huevos es: ₵", precio)

    menu = int(input("\nIngrese la opción del menú: "))

    if menu == 2:
        print("\n***¡Gracias comprar huevos con nosotros!***")


##############Final
