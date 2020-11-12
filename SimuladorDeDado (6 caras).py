import random

pregunta = "Si desea tirar el dado, escriba 'S': "

def respuesta():
    return (input(pregunta))

while respuesta() == "S":
    print (random.choice(range(1,7)))