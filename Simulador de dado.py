#Simulador de dado

import random

pregunta = (input("¿Desea tirar el dado? "))
dado = random.choice(range(1,6))

if pregunta == "S":
    print ("El número del dado es:", dado)
#No consigo introducir una iteración While para que siga preguntando hasta que conteste "no"