#solicita los datos al usuario
horasTrabajadas= float(input("Ingrese la cantidad de horas trabajadas en la semana "))
precioHora= float(input("Ingrese el precio por hora: "))

#realiza las operaciones
salarioMensual = horasTrabajadas * precioHora * 4.2
cargasSociales = salarioMensual * 0.105
asociacion = salarioMensual * 0.05

#Imprime el mensaje con los resultados
print("El salario mensual es ",salarioMensual)
print("Las cargas sociales son", cargasSociales)
print("El monto por asociacion solidarita", asociacion)

#calcula el resultado en la misma opción de imprimir
print("El salario mensual neto es", salarioMensual-cargasSociales-asociacion)
