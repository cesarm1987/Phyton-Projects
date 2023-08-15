horasTrabajadas = [["Lunes  ", 0],
                   ["Martes ", 0],
                   ["Miercoles", 0],
                   ["Jueves  ", 0],
                   ["Viernes ", 0],
                   ["Sabado   ", 0]]
x = 0
y = 0


CCSS = 0.09
ASOC = 0.05
BP = 0.01
opcion= 0

def nombre():
    name = input("Ingrese su nombre:")
    print("Nombre del empleado:",name)
def IngresarDatos():

    for x in range(0, 6):
        for y in range(0, 1):
            horas= input("Ingrese las horas laboradas: ")
            horasTrabajadas[x][1] = horas

def TotaldeHorasTrabajadas():
    Suma= 0
    for x in range(0, 6):
        for y in range(0,2):
            if y == 1:
                Suma = Suma + int(horasTrabajadas[x][1])

    return(Suma)


def Mayor():
    MayorHoras = 0
    days = ''
    x=0
    y=0
    max = horasTrabajadas[x][y]
    for x in range(0,6):
        for y in range(0,2):
            if (int(horasTrabajadas[x][1])>MayorHoras):
                MayorHoras = int(horasTrabajadas[x][1])
                days= horasTrabajadas[x][y]

    print("El dia mas laborado es el",days,"con",MayorHoras,"horas")

def SalarioBruto():

    Suma = TotaldeHorasTrabajadas()
    pagoxhora = 2500
    salario = 0

    if Suma== 0:
        print("Dato invalido")
    elif Suma <= 40:
        salario = Suma * pagoxhora
        print("Total de horas ordinarias laboradas: ", Suma
                      , "\nSalario :", salario)

    elif Suma > 40:
        hrs = 40
        horas_adicionales = Suma - hrs
        hora_extra = pagoxhora * 2
        salario = (hrs * pagoxhora) + (horas_adicionales * hora_extra)
        montoDev = horas_adicionales * hora_extra
        print("Total de horas laboradas:     ",Suma,
            "\nTotal de horas extras:        ",horas_adicionales,
            "\nMonto devengado x hors extras:",montoDev,
            "\nSalario:                      ",salario)

    return(salario)

def SalarioNeto():
    salario = SalarioBruto()

    ccss = salario * CCSS
    bp = salario * BP
    asoc = salario * ASOC
    total= ccss + bp + asoc
    salneto = salario- total
    print("CCSS:             ",ccss,
          "\nBanco Popular:    ",bp,
          "\nAsoc.Solidarista: ",asoc,
          "\nTotal deducciones:",total,
          "\nSalario Neto:     ",salneto)

def Imprimir():
    for x in range(0, 6):
        for y in range(0, 2):
            print(horasTrabajadas[x][y], end=" ")
        print("\n")

def Menu():

    opcion = int(input("Bienvenido! "
                       "\n1. Ingresar horas.  "
                       "\n2. Dia mas laborado.  "
                       "\n3. Salario Bruto. "
                       "\n4. Salario Neto. "
                       "\n5. Salir."
                       "\n Seleccione una opcion:"))

    if opcion == 1:
        IngresarDatos()
        Imprimir()
    elif opcion == 2:
        Mayor()
    elif opcion == 3:
        SalarioBruto()
    elif opcion == 4:
        SalarioNeto()
    elif opcion == 5:
       exit()

def Ejecucion():
    nombre()
    while opcion != 5:
        Menu()



Ejecucion()


