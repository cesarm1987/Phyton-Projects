personas = 0
rooms = 0
y = 0
acompanante = []
ced_acomp = []
edad_acomp=[]
reservday = []
z = 0
iva = 0
total = 0
option = 0
pers = []
num_mesa = []
tiemp_com = []
hora = []
mes = []



def Registrohotel():

 X = input("Bienvenido a la cadena de hoteles El descanso, ingrese el nombre del hotel que desea hospedarse: ")
 if X == "Puntarenas":
    personas = int(input("Ingrese la capacidad total del hotel(personas): "))
    rooms = int(input("Ingrese la cantidad total de habitaciones: "))
    aforo = int(input("Ingrese el aforo aprobado por el Ministerio de Salud: "))
    c_aforo= int(rooms*(aforo/100))
    print("................................")
    print("Excelente seleccion!")
    print("El hotel escogido es El descanso- Puntarenas")
    print("Actualmente contamos con el",aforo,"% del aforo en habitaciones")
    print("Habitaciones disponibles:", c_aforo)

 elif X == "San Carlos":
     personas = int(input("Ingrese la capacidad total del hotel(personas): "))
     rooms = int(input("Ingrese la cantidad total de habitaciones: "))
     aforo = int(input("Ingrese el aforo aprobado por el Ministerio de Salud: "))
     c_aforo = int(rooms * (aforo / 100))
     print("................................")
     print("Excelente seleccion!")
     print("El hotel escogido es El descanso- San Carlos")
     print("Actualmente contamos con el", aforo, "% del aforo en habitaciones")
     print("Habitaciones disponibles:", c_aforo)

 elif X == "Guanacaste":
     personas = int(input("Ingrese la capacidad total del hotel(personas): "))
     rooms = int(input("Ingrese la cantidad total de habitaciones: "))
     aforo = int(input("Ingrese el aforo aprobado por el Ministerio de Salud: "))
     c_aforo = int(rooms * (aforo / 100))
     print("................................")
     print("Excelente seleccion!")
     print("El hotel escogido es El descanso- Guanacaste")
     print("Actualmente contamos con el", aforo, "% del aforo en habitaciones")
     print("Habitaciones disponibles:", c_aforo)

 else:
   print("Valor invalido")



def Registrocliente():
    i=0
    acomp = 0
    nombre = input("Ingrese su nombre: ")
    cedula= int(input("Por favor digite su numero de cedula: "))
    pais = input("Ingrese el pais de residencia: ")
    provincia = input("Ingrese la provincia en la que vive: ")
    canton = input("Ingrese el canton en el que vive: ")
    distrito = input("Ingrese el distrito en el que vive: ")
    edad = int(input("Ingrese su edad: "))
    pago = input("Ingrese su metodo de pago: ")
    opc = input("Trae acompañantes?  s/n:")
    if opc == "s":
        acomp= int(input("Ingrese el numero de acompañantes: "))
        for i in range(acomp):

         nombrec = input("Ingrese el nombre del acompañante: ")
         cedulac = int(input("Por favor digite el numero de cedula: "))
         edadc = int(input("Ingrese la edad de su acompañante: "))
         nombrec= acompanante.append(nombrec)
         cedulac = ced_acomp.append(cedulac)
         edadc = edad_acomp.append(edadc)
    elif opc == "n":
        Ejecucion()

    print("..........CONFIRMACION..........."
        "\nNombre del cliente:  ", nombre,
          "\nNumero de cedula:  ", cedula,
          "\nPais de origen:    ", pais,
          "\nProvincia:         ", provincia,
          "\nCanton:            ", canton,
          "\nDistrito:          ", distrito,
          "\nEdad:              ", edad,
          "\nMetodo de pago:    ", pago,
          "\n                               "
          "\n**INFORMACION DEL ACOMPAÑANTE**"
          "\n                               "
          "\nNumero de acompañantes: ",acomp,
          "\nNombre: ",acompanante,
          "\nNumero de cedula: ",ced_acomp,
          "\nEdad: ",edad_acomp)

def Consultar():
    Tipo_habitacion = int(input("Tipo de habitaciones:\n1.Standar. \n2.Familiar. \nQue tipo de habitacion desea consultar:"))
    if Tipo_habitacion == 1:
        print("................................"
            "\nHabitacion Estandar: \nMaximo 2 personas."
              "\nIncluye servicios."
              "\nTarifa por noche: $300")
        print("...................................")
    elif Tipo_habitacion == 2:
        print("......................................."
              "\nHabitacion Familiar: \nMaximo 4 personas."
              "\nIncluye servicios."
              "\nTarifa por noche: $600")
        print("...................................")

def Reservacion():
      dias=[]
      tarifa=0
      days = int(input("Cuantos dias se desea hospedar: "))
      for i in range(days):
       dias_hosp = input("Ingrese el dia: ")
       dias_hosp = dias.append(dias_hosp)

      habitacion=int(input("Que tipo de habitacion desea? \n1.Estandar \n2.Familiar. \nElija la que desee:"))
      if habitacion == 1:
          personas_hos = int(input("Ingrese el numero de personas: "))
          if personas_hos > 2:
              exit("El numero de personas excede la capacidad permitia por habitacion ")
          else:
              tarifa= (personas_hos * 300)*days
      elif habitacion == 2:
        personas_hos = int(input("Ingrese el numero de personas: "))
        if personas_hos > 4:
            exit("El numero de personas excede la capacidad permitia por habitacion ")
        elif personas_hos == 4:
            tarifa = (personas_hos * 600)*days
      print("...................................")
      print("Los dias reservados son:",dias)
      print("La tarifa por dias reservados es de: $",tarifa)
      iva = tarifa * 0.13
      precio_total= tarifa + iva
      print("IVA: $",iva)
      print("Precio total: $",precio_total)
      print("...................................")


def Restaurante():


    mesa = int(input("Cuantas mesas desea reservar: "))
    person= int(input("Ingrese el numero de personas: "))
    numero_mesa= int(input("Ingrese el numero de mesa: "))
    tiemp_comida= input("Ingrese el tiempo de comida: ")
    time = input("Ingrese la hora que desea hacer la reserva: ")
    person = pers.append(person)
    numero_mesa=num_mesa.append(numero_mesa)
    tiemp_comida=tiemp_com.append(tiemp_comida)
    time = hora.append(time)

def MostrarReservacion():
    opc = int(input("Reservacion de Restaurante: \n1.Reservacion."
                    "\n2.Mostrar Reservacion."
                    "\n3.Regresar al menu principal"
                    "\nElija una opcion: "))

    if opc ==1:
        Restaurante()
    elif opc ==2:
        print("+++++++RESERVACION+++++++++"
            "\nNumero de personas: ",pers,
            "\nNumero de mesa:    ",num_mesa,
            "\nTiempo de comida:   ",tiemp_com,
            "\nHora:               ",hora)
        print("...................................")
    elif opc == 3:
        Menu()

def Menu():
    opcion = int(input("Bienvenido a la cadena de hoteles El descanso !"
                       "\n                                       "
                       "\n------------Menu Principal--------"
                       "\n                                     "
                       "\n1. Registro del Hotel.  "
                       "\n2. Registro del Cliente.  "
                       "\n3. Consultar Habitaciones. "
                       "\n4. Rerservaciones de Hospedaje. "
                       "\n5. Reservaciones de Restaurante."
                       "\n6. Horarios de Ingreso y Salida."
                       "\n7. Salir"
                       "\n   Seleccione una opcion: "))

    if opcion == 1:
       Registrohotel()
    elif opcion == 2:
       Registrocliente()
    elif opcion == 3:
       Consultar()
    elif opcion == 4:
       Reservacion()
    elif opcion == 5:
       Ejecutando()
    elif opcion == 6:
        InOut()
    elif opcion == 7:
        exit()

def InOut():
    ingreso = input("Ingrese la hora del checkin: ")
    salida = input("Ingrese la hora del checkout: ")
    print("...........................")
    print("Su ingreso es a las:",ingreso)
    print("Su salida es a las:", salida)
    print("............................")

def Ejecutando():
    while option != 3:
      MostrarReservacion()

def Ejecucion():
    while option != 7:
      Menu()

Ejecucion()



