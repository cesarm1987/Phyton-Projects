#PRACTICA 4
x=1
print("Juego del abecedario\n")
while x==1:
    y=input("Ingrese una letra: \n")
    if y == "a" or y=="e" or y=="i" or y=="o" or y=="u" or y=="A" or y=="E" or y=="I" or y=="O" or y=="U":
        print("La letra es una vocal!\n")
    else:
        if y == "b" or y=="c" or y=="d" or y=="f" or y=="g" or y=="h" or y=="j" or y=="k" or y=="l"or y=="m" or y=="n" or y=="p" or y=="q" or y=="r" or y=="s" or y=="t" or y=="v" or y=="w" or y=="x" or y=="y" or y=="z" or y=="ñ" or y=="B" or y=="C" or y=="D" or y=="F" or y=="G" or y=="H" or y=="J" or y=="K" or y=="L" or y=="M" or y=="N" or y=="P" or y=="Q"or y=="R" or y=="S" or y=="T" or y=="V" or y=="W" or y=="X" or y=="Y" or y=="Z" or y=="Ñ":
            print("La letra no es una vocal\n")
        else:
            print("El caracter ingresado no es consonante ni vocal\n")
    x=int(input("\nDesea jugar otra vez, escoja un número? 1- Si    2- No: \n"))
print("Gracias por jugar! \n")