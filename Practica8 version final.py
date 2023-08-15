import os

empleados=[]
i = 0
opcion = 0
def crearArchivo():
    file = open("PracticaArchivos2.txt","w")
    print("El archivo ha sido creado exitosamente")
    file.close()

def IngresarDatos():
    file = open("PracticaArchivos2.txt", "a")
    n = int(input("Dijiete el nummero de empleados que desea registrar: "))
    for x in range(n):
         Nombre = input("Ingrese el nombre del empleado: ")
         empleados.append(Nombre)
    file.write('Empleados=%s'%empleados)
    file.write("\n")
    file.close()

def ConsultarEmpleado():
    file = open("PracticaArchivos2.txt","a")
    nombre = input("Ingrese el nombre del empleado: ")
    for x in range(len(empleados)):
      if nombre == empleados[x]:

       file.write('El usuario=%s'%empleados[x]+', ya existe')
       file.write("\n")
    file.close()
def Modificar():
    file = open("PracticaArchivos2.txt", "a")
    oldname= input("Ingrese el nombre que quiera actualizar:")
    newname= input("Ingrese el nombre:")
    for x in range(len(empleados)):
        if oldname == empleados[x]:
            empleados[x]=newname
            file.write('Se ha actualizado el usuario=%s' % oldname + ',por'+ empleados[x])
            file.write("\n")
    file.write('Empleados=%s'%empleados)
    file.close()

def Eliminar():
    file = open("PracticaArchivos2.txt", "a")
    nombre = input("Ingrese el nombre que desea eliminar:")
    for x in range(len(empleados)-1,-1,-1):
        if nombre == empleados[x]:
            file.write('Se ha eliminado el usario=% s'%empleados.pop(x))
            file.write("\n")
            file.write('Empleados=%s' % empleados)
    file.close()
def MostraInformacion():
    file = open("PracticaArchivos2.txt","r")
    mensaje = file.read()
    print(mensaje)
    file.close()

def Menu():
    opcion = int(input("Bienvenido al Sistema CA! \nQue desea hacer:"
                       "\n1. Crear Archivo nuevo "
                       "\n2. Ingresar Empleados."
                       "\n3. Consultar"
                       "\n4. Modificar."
                       "\n5. Eliminar"
                       "\n6. Imprimir"
                       "\n7. Salir"
                       "\n Elija una opcion: "))

    if opcion == 1:
       crearArchivo()
    elif opcion == 2:
        IngresarDatos()
    elif opcion == 3:
        ConsultarEmpleado()
    elif opcion == 4:
        Modificar()
    elif opcion == 5:
       Eliminar()
    elif opcion == 6:
        MostraInformacion()



def ejecucion():
    while opcion != 7:
        Menu()


ejecucion()