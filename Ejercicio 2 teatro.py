#Ejercicio 2
'''En una sala de teatro se requiere almacenar los nombres de las
personas que ocuparán las butacas de una fila, cada fila tiene 10 butacas.
Cree un programa que almacena los nombres en las posiciones que le van indicando
, por ejemplo:  Ana Jiménez, 4 (el cuatro indica el número de butaca).'''

opcion = "s"
fila = []
for x in range(10):
    fila.append(" ")
while opcion =="s" or opcion =="S":
    reserva = str(input("Digite su nombre: "))
    butaca = int(input("Digite una butaca del 1 al 10: "))
    if fila[butaca-1]== " " :
        fila[butaca-1]= reserva
    else:
        print("La butaca escogida está ocupada, vuelva a intentarlo")
    opcion= input("Desea ingresar otra reserva s/S: ")

#Despliega las reservas existentes

for x in range(10):
    print(f"Butaca {x+1} , {fila[x]}")
        


