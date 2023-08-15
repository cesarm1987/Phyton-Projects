salarioActual=0.00
antiguedad=0
salarioActual=float(input("Digite el salario actual: "))
antiguedad=int(input("Digite la antiguedad del empleado: "))
if ((antiguedad>=0)and(antiguedad<=5)):
    salarioActual=salarioActual*1.01
elif((antiguedad>=6)and(antiguedad<=10)):
    salarioActual=salarioActual*1.03
elif((antiguedad>=11)and(antiguedad<=13)):
    salarioActual=salarioActual*1.05
else:
    salarioActual=salarioActual*1.07
print("El salario luego del aumento es: ",salarioActual)
