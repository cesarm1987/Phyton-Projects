#Solicita la información al usuario

juego=input("Desea jugar a adivinar vocales, presione Y o y: ")

#Utiliza ciclo para indicar si es una vocal.

while juego == "Y" or juego == "y":
    letra=input("Digite una letra: ")
    if letra == "A" or  letra == "a" or letra =="E" or letra =="e" or letra == "I" or letra =="i" or letra =="O" or letra =="o" or letra =="U" or letra =="u":
        print("La letra", letra,"si es una vocal: ")
    else:
        print("La letra",letra,"no es una vocal: ")
    juego=input("Desea seguir jugando presione Y o y, sino digite cualquier otra letra: ")
print()
print("****El juego finalizo****")
