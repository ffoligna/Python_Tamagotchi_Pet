#Simulador de dado

import random

pregunta = (input("¿Desea tirar el dado? "))
dado = random.choice(range(1,6))

if pregunta:
    print ("El número del dado es:", dado)
    while pregunta == "S":
        print (input("¿Desea tirar el dado? "))
#No consigo introducir una iteración While para que siga preguntando hasta que conteste "no". Nunca termina de imprimir "S"