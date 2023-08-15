def aplazados(calif):
    contador = 0
    for i in range(10):
        if calif[i]< 70:
            contador += 1
    print("\n\n *****ESTUDIANTES QUE PERDIERON LA MATERIA*****")
    print(f"\n{contador} estudiantes perdieron la materia")

def mayor_menor(nombres,calif):
    mayor = calif[0]
    menor= calif[0]
    indicea = 0
    indiceb = 0
    for i in range(10):
        if calif[i]> mayor:
            mayor = calif[i]
            indicea = i
        if calif[i]< menor:
            menor = calif[i]
            indiceb = i
    print("\n\n *****ESTUDIANTES CON NOTA MÁS ALTA Y BAJA*****")
    print(f"\nEl estudiante {nombres[indicea]} tiene la nota más alta: {mayor}")
    print(f"\nEl estudiante {nombres[indiceb]} tiene la nota más baja: {menor}")

def evalua_docente(nombres,calif):
    print("\n\n")
    print("*****Las notas después de la evaluación docente quedan así*****\n\n")
    for i in range(10):
        calif[i]+=3
        if calif[i]> 100:
            calif[i]= 100 
        print(f"La nota del estudiante {nombres[i]} es: {calif[i]}")

def despliega_notas(nombres,calif):
    print("\n\n *****NOTAS DE LOS ESTUDIANTES*****\n\n")
    for i in range(10):
        print(f"La nota del estudiante {nombres[i]} es: {calif[i]}")


#PRINCIPAL
#Crear un arreglo para nombres y uno para notas
notas = []
estudiantes= []

for i in range(10):
    estudiantes.append([" "])
    notas.append([0])


#Ingresa las notas y nombres de los  estudiantes

for i in range(10):
    estudiantes[i]= input("Ingrese el nombre del estudiante: ")
    notas[i]= int(input("Ingrese la nota del estudiante: "))

despliega_notas(estudiantes,notas)
evalua_docente(estudiantes,notas)
mayor_menor(estudiantes,notas)
aplazados(notas)
