#!/usr/bin/python

# -*- coding: utf-8 -*-
import os 

print ("\nBienvenidos al calcular de Gallinas...\n") #Saludo de bienvenida
input("Digite una tecla para continuar...") # Se pulsa una tecla para continuar

#Definimos una funcion para el menu que se va mostar 
def menu():

	"""

	Función que limpia la pantalla y muestra nuevamente el menu

	"""

	os.system('cls') # limpia la pantalla

	print ("+---------------------------------------------------+")
	print ("|                                                   |")
	print ("|              Prueba Corta #2                      |")
	print ("| \t1 - Calculo de precio                       |")
	print ("| \t9 - salir                                   |")
	print ("|                                                   |")
	print ("+---------------------------------------------------+")

#Declaramos variables
peso_Gallina = 0.0
altura_Gallina = 0.0
huevos = 0
promedio_Calidad = 0.0
precio_Huevo = 0.0

while True:
    #Mostramos las opciones del menu, mientras se mantenga dentro de este va seguir preguntando por las opciones, hasta que se prescione las opciones correspondientes.
    menu()

    # Le solicitamos al usuario que ingrese la opcion que dese ejecutar y este se lo asignamos a la variable opcionMenu
    opcionMenu = input("inserta la opcion que desea Ejecutar >> ")

    #El menu solo es de 2 opciones.
    if opcionMenu =="1":
        #Solicitamos al usuario ingresar los datos de la gallina, y ahi mismo se realiza la operacion para saber el Promedio de Calidad

        peso_Gallina =float (input("\n\nDigite el Peso de la gallina en Kilogramos\n"))
        altura_Gallina =float (input("\n\nDigite la Altura de la gallina en centimetros\n"))
        huevos =int (input("\n\nDigite la cantidad de huevos que pone la gallina\n"))
        promedio_Calidad =float (peso_Gallina * altura_Gallina) / huevos

        #Ahora vamos a seleccionar cual va ser el precio por kilo de huevos

        if promedio_Calidad >= 15:  #Si el promedio de calidad es mayor o iggual que 15
            precio_Huevo = 1.2 * promedio_Calidad
            print ("El promedio de Calidad de la Gallina es : ",promedio_Calidad,",","y", " El Precio por kilo de huevos en colones es : ",precio_Huevo)
            input("Digite una tecla para continuar...")
            

        elif promedio_Calidad >8  < 15: #Si el promedio de calidad es mayor que 8 y menor que 15
            precio_Huevo = 1.00 * promedio_Calidad
            print ("El promedio de Calidad de la Gallina es : ",promedio_Calidad,",","y", " El Precio por kilo de huevos en colones es : ",precio_Huevo)
            input("Digite una tecla para continuar...")
            

        elif promedio_Calidad <= 8:  #Si el romedio de calidad es menor o igual que 8
            precio_Huevo = 0.80 * promedio_Calidad
            print ("El promedio de Calidad de la Gallina es : ",promedio_Calidad,",","y", " El Precio por kilo de huevos en colones es : ",precio_Huevo)
            input("Digite una tecla para continuar...")
            

    elif opcionMenu == "9": #Si 
        print("Gracias por Utilizar el calcular de Precio de Huevo de Gallina y Calidad del mismo...\nVuelva Pronto...\n")
        break

    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
		

   

