ingresos=0
gastos=0
print("Ejercicio 1")
ingresos = int(input("\n Ingrese el monto en colones de sus ingresos mensuales: "))
gastos = int(input("\n Ingrese el monto en colones de sus gastos mensuales por alimentacion: "))
porcentajeAlimentacion=gastos*100/ingresos
porcentajeGastosVarios=100-porcentajeAlimentacion
print("\n El porcentaje de sus gastos por alimentacion es de: %", porcentajeAlimentacion, "y el porcentaje de sus ingresos destinado a otros montos es de: %", porcentajeGastosVarios)
