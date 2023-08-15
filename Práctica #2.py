#solicita los datos al usuario
ingresos= float(input("Incluya el monto de sus ingresos "))
gastos= float(input("Incluya el monto de sus gastos de alimentación "))

#realiza las operaciones
porcentajeAlimentacion = (gastos/ingresos)*100


#Imprime el mensaje con los resultados
print("El porcentaje de alimentación es ", porcentajeAlimentacion, "% y el porcentaje disponible", 100-porcentajeAlimentacion, "%")


