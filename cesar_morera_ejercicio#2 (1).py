# Declaracion de las variables

Monto_Dev = 0
hora_extra = 0
horas_adicionales = 0
pagoxhora = 10000
CCSS_CONTRIBUTION = 0.09
BANCO_POPULAR_CONTRIBUTION = 0.01
ASOCIACION_SOLIDARISTA_CONTRIBUTION = 0.05

# Solicitud de datos del trabajador

name = input("Porfavor ingrese su nombre: ")
horas = int(input("Porfavor ingrese las horas laboradas: "))

# Calculo de horas trabajadas

if horas == 0:
    exit("Dato invalido")
elif horas <= 40:

    salario = horas * pagoxhora

elif horas > 40:
    hrs = 40
    horas_adicionales = horas - hrs
    hora_extra = int(pagoxhora * 0.5) + pagoxhora
    salario = hrs * pagoxhora

# Calculos de deducciones por ley

Monto_Dev = hora_extra * horas_adicionales
ccss = int((salario + Monto_Dev) * CCSS_CONTRIBUTION)
BPD =  int((salario + Monto_Dev) * BANCO_POPULAR_CONTRIBUTION)
ASS =  int((salario + Monto_Dev) * ASOCIACION_SOLIDARISTA_CONTRIBUTION)


total_deductions = int((ccss + BPD + ASS))
salario_neto = Monto_Dev +salario - total_deductions

# Impresion de resultados finales

print("Nombre del empleado:              ",name)
print("Salario bruto:                    ",salario)
print("Monto devengado por horas extras: ",Monto_Dev)
print("9% CCSS:                          ",ccss)
print("1% Banco Popular:                 ",BPD)
print("5% Asociacion Solidarista:        ",ASS)
print("Total de deducciones:             ",total_deductions)
print("Salario Neto:                     ",salario_neto)

