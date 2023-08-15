personas = 0
rooms = 0
y = 0
acpt = []
reservday = []
z = 0
iva = 0
total = 0



class Registrohotel:

 X = str(input("Bienvenido a la cadena de hoteles El descanso, ingrese el nombre del hotel que desea hospedarse Puntarenas, Guanacaste o San Carlos: "))
 if X == "Puntarenas":
    print("Excelente seleccion")
    print("El hotel escogido es El descanso- Puntarenas")
    rooms = 120 * 4
    print("Contamos con una capacidad total de", rooms)
    print("Contamos con", 120,"habitaciones")
    print("Actualmente contamos tambien con el 100% del aforo en habitaciones")

 elif X == "San Carlos":
     print("Excelente seleccion")
     print("El hotel escogido es El descanso- San Carlos")
     rooms = 60 * 2
     print("Contamos con una capacidad total de", rooms)
     print("Contamos con", 60, "habitaciones")
     print("Actualmente contamos tambien con el 100% del aforo en habitaciones")

 elif X == "Guanacaste":
  print("Excelente seleccion")
  print("El hotel escogido es El descanso- Guanacaste")
  rooms = 100 * 4
  print("Contamos con una capacidad total de", rooms)
  print("Contamos con", 100, "habitaciones")
  print("Actualmente contamos tambien con el 100% del aforo en habitaciones")

 else:
   print("Valor invalido")

pass;

class Registrocliente:
    nombre = input("Ingrese su nombre: ")
    cedula= int(input("Por favor digite su numero de cedula: "))
    pais = input("Ingrese el pais de residencia: ")
    provincia = input("Ingrese la provincia en la que vive: ")
    canton = input("Ingrese el canton en el que vive: ")
    distrito = input("Ingrese el distrito en el que vive: ")
    edad = int(input("Ingrese su edad: "))
    pago = input("Ingrese su metodo de pago: ")
    acomp= int(input("Ingrese el numero de acompañantes: "))

    for i in range(acomp):
        acpt.append(" ")

    while y != acomp:
        nombrec = input("Ingrese el nombre del acompañante: ")
        cedulac = int(input("Por favor digite el numero de cedula: "))
        edadc = int(input("Ingrese la edad de su acompañante: "))
        acpt[y] = nombrec
        y += 1
        i = y

pass;

class Reservacion:
      dias = int(input("Ingrese los dias de hospedaje: "))
      days = int(input("Que dias se va a quedar hospedado: \n1.L-Mr \n2.M-J \n3.Mr-V \n4.V-D \n5.S-L"))

      if days == 1:
         tarifa = 100 * 3
         print("El aforo para los dias Lunes, Martes y Miercoles es del 100%")

      elif days == 2:
          tarifa = 100 * 3
          print("El aforo para los dias Martes, Miercoles y Jueves  es del 100%")

      elif days == 3:
          tarifa = 100 * 3
          print("El aforo para los dias Miercoles, Jueves y Viernes es del 100%")

      elif days == 4:
          tarifa = (100 * 0.2) + 100 * 2 + 100
          print("El aforo para Los dias Viernes, Sabado y Domingo es del 50%")

      elif days == 5:
           tarifa = (100 * 0.2) + 100 * 2 + 100
           print("El aforo para Los dias Sabado, Domingo y Lunes es del 50%")

      else :
           exit("Valor invalido")

pass;


class Restaurante:
      dias = input("Ingrese el dia que desea reservar en el restaurante: ")
      tiempo = input("Indique el tiempo: ")
      horas = int(input("Indique la hora que desea asistir: "))
pass;


class InOut:
    ingreso = input("Ingrese la hora del checkin: ")
    salida = input("Ingrese la hora del checkout: ")
pass;

print("Nombre del cliente: ",Registrocliente.nombre)
print("Numero de cedula: ",Registrocliente.cedula)
print("Pais: ",Registrocliente.pais)
print("Distrito: ",Registrocliente.distrito)
print("Provincia: ",Registrocliente.provincia)
print("Canton: ",Registrocliente.canton)
print("Edad: ",Registrocliente.edad)
print("Tipo de pago: ",Registrocliente.pago)
for i in range(Registrocliente.acomp):

    print("Acompañantes: ",acpt[i])

iva = float(Reservacion.tarifa * 0.13)
total = Reservacion.tarifa + iva

print("Dias: ",Reservacion.dias)
print("Tarifa a pagar: ",Reservacion.tarifa)
print("IVA: ",iva)
print("Total a pagar: ",total)
print("Dias de reservacion: ",Restaurante.dias)
print("Tiempos de comida: ",Restaurante.tiempo)
print("Hora de reservacion: ",Restaurante.horas)

print("Checkin: ",InOut.ingreso)
print("Checkout: ",InOut.salida)


