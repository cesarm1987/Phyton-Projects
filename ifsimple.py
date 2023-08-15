salarioActual=0.00
antiguedad=0
nuevoSalario=0.00
salarioActual=float(input("Digite el salario actual del empleado: "))
antiguedad=int(input("Digite los años de antiguedad del empleado: "))
if(antiguedad>5):
    salarioActual=salarioActual*1.10;
print("El nuevo salario del empleado es:",salarioActual)
