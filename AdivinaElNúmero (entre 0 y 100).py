#El programa genera un número aleatorio y después le pide al ususario
#que adivine el mismo. Lo va guiando según sea más grande o más chico
#con la leyenda "El número es muy grande" o "El número es muy chico".
#Cuando el ususario acierta el número, una leyenda se lo indica y el
#programa termina. Además. el usuario tiene "vidas" o intentos máximos
#para poder adivinar y se le indica cuántos intentos le quedan.

import random

number = random.randint(0, 100)
lives = 7

while lives > 0:
    print ("Tienes", lives, "intento/s para adivinar.")
    question = input("¿Cuál es el número que elegí del 0 al 100?: ")
    lives = lives - 1
    while not (question.isdigit()):
        question = input("""El dato ingresado no es un número.
Por favor, ingrese un número del 0 al 100: """)
    if int(question) > number and lives > 0:
        print("El número es muy grande")
    if int(question) < number and lives > 0:
        print("El número es muy chico")
    if int(question) == number and lives > 0:
        print("¡Adivinaste! El número es", number)
        break
    if lives == 0:
        print("Te quedaste sin intentos. Has perdido.")
