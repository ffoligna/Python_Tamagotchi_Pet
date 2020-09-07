#Simulador de dado

import random

pregunta = (input("¿Desea tirar el dado? "))
dado = (random.choice(range(1,6)))

while pregunta == "S":
    pregunta = (input("¿Desea tirar el dado? "))
    print (random.choice(range(1,6)))

#La primera vez que pregunta, si respondes S te vuelve a preguntar en vez de imprimir el número. Cuando pasas esa instancia,
#si contestás otra cosa, igual te imprime un número y ahí termina el loop.