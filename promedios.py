nota1 = int(input("Dame la nota 1: "))
nota2 = int(input("Dame la nota 2: "))
nota3 = int(input("Dame la nota 3: "))
promedio = (nota1 + nota2 + nota3) /3
if promedio >= 70:
    print ("Aprobado")
else:
    if promedio >= 60:
        print("Ampliacion")
    else:
        print("Reprobado")