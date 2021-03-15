#Programa para obtener el resultado de interés simple

montoInicial = int(input("Introduzca un monto sin decimales: "))
montoFinal = montoInicial
i = float(input("Introduzca el interés anual: "))
n = int(input("Introduzca la cantidad de meses: "))
mes = 0

for x in range(n):
	montoFinal = montoFinal * (((i / 12) / 100) + 1)
	mes = mes + 1
	print(f"Monto del mes {mes} es {montoFinal}")

interesAcumulado = (((montoFinal - montoInicial) * 100) / montoInicial)

ganancia = montoFinal - montoInicial

print(f"El monto inicial es: ${montoInicial}")
print(f"La ganancia es: ${ganancia}")
print(f"El monto final en {mes} meses es: ${montoFinal}")
print(f"El interés acumulado en {n} meses es: {interesAcumulado}%.")
