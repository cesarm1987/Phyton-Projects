
def imprime(kilosem):

    cantidad = 0

    for x in range(7):
        if x+1 == 1:
            print("El lunes corrió \t", kilosem[x], "kilómetros")
        elif x+1 == 2:
            print("El martes corrió \t", kilosem[x], "kilómetros")       
        elif x+1 == 3:
            print("El miércoles corrió \t", kilosem[x], "kilómetros") 
        elif x+1 == 4:
            print("El jueves corrió \t", kilosem[x], "kilómetros")
        elif x+1 == 5:
            print("El viernes corrió \t", kilosem[x], "kilómetros")
        elif x+1 == 6:
            print("El sábado corrió \t", kilosem[x], "kilómetros")
        elif x+1 == 7:
            print("El domingo corrió \t", kilosem[x], "kilómetros")
        cantidad += kilosem[x]

    print("\nEn la semana corrío \t", cantidad, "kilómetros")


#Solicitud de información
semana =[]
dias=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
print("Ingresar la cantidad de kilómetros por día de lunes a domingo")
for x in range(7):
    kilometro = int(input(f"Ingrese cantidad de kilómetros del día {dias[x]}:\t"))
    semana.append(kilometro)

imprime(semana)
print()
print("***Gracias por usar nuestro programa***")
