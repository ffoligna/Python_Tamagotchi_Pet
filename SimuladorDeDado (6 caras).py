#Este programa simula la tirada de un dado de 6 caras e imprime su resultado
#aleatorio. Después de imprimirlo, pregunta si el ususario desea volver a
#tirar el dado. Si se ingresa otra letra que no sea "S", el programa
#imprime una leyenda indicando que la letra es erronea y deja de funcionar.

import random

question = "Si desea tirar el dado, escriba 'S': "

def answer():
    return input(question)

while answer().upper() == "S":
    print(random.choice(range(1, 7)))
else:
    print("Usted ha ingresado una letra errónea. El programa se ha cerrado.")
    