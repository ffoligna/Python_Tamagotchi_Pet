#Programa para obtener interés compuesto con incremento de capital mes a mes

m = int(input("Ingrese el monto mensual: "))
i = float(input("Ingrese el interés anual: "))
n = int(input("Ingrese la cantidad de meses: "))
mes = 0
montoInicial = 117000

for x in range(n):
	montoInicial = (montoInicial + m) * (((i / 12) / 100) + 1)
	mes = mes + 1
	print(f"Monto del mes {mes} es {montoInicial:.2f}")

montoFinal = montoInicial

print(f"El monto final después de {n} meses es {montoFinal:.2f}")
