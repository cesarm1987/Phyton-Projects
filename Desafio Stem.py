#solicita los datos al usuario, carga y define las variables
identificacion= str(input("Escriba su identificacion "))
nombre = str(input("Escriba su nombre "))
salarioBruto= float(input("Ingrese el monto de su salario bruto "))

#realiza las operaciones

CCSS = salarioBruto * 0.08
BcoPop = salarioBruto * 0.01
totalDeducciones = CCSS + BcoPop
salarioNeto = salarioBruto - totalDeducciones

#Imprime el mensaje con los resultados
print("Nombre         ", nombre)
print("Identificacion        ", identificacion)
print("Salario bruto         ", round(salarioBruto,2))
print("CCSS (8%)             ", round(CCSS,2))
print("Banco Popular (1%)    ", round(BcoPop,2))
print("Total de deducciones",   round(totalDeducciones,2))
print("Salario neto        ",  round(salarioNeto,2))
