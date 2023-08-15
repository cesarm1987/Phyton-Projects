#Inclusión de la librería RANDOM
import random

valor = random.random()#genera un número entre 0 y 0.99
print(valor)#presenta el número generado con decimales 
print(valor * 100) #presenta el número entre 1 y 100 con decimales
print(int(valor*100))#presenta el número entero entre 1 y 100
print(int(random.random()*100))

print(int(random.randrange(50,100)))
