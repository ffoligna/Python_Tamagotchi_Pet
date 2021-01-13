import random

número = random.randint(0, 100)


while número:
    pregunta = input("¿Cuál es el número que elegí del 0 al 100? ")
    if int(pregunta) > número:
        print("El número es muy grande")
    if int(pregunta) < número:
        print("El número es muy chico")
    if int(pregunta) == número:
        print("¡Adivinaste! El número es", número)
        break
