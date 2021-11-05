# Tamagotchi, tu mascota virtual.
# Versión remasterizada por Federico Foligna (Agosto-2021)

import cmd
import textwrap
import sys
import os
import time
import random

class Tamagotchi:
    tipo = random.choice(["Genbu", "Suzaku", "Byakko", "Seiryu"])
    nombre = ""
    fuerza = 0
    hambre = 0
    animo = 0
    cansancio = 0

    def __init__(self, nombre, fuerza, hambre, animo, cansancio):
        self.nombre = nombre
        self.fuerza = fuerza
        self.hambre = hambre
        self.animo = animo
        self.cansancio = cansancio

    def ejercitar(self):
        self.fuerza += random.randint(2,4)
        self.hambre += random.randint(2,4)
        self.cansancio += random.randint(1,3)
        self.animo -= random.randint(2,3)

        ejercitar1 = "\nMe estoy ejercitando!\nGo Go Go!\n"
        for letras in ejercitar1:
            sys.stdout.write(letras)
            sys.stdout.flush()
            time.sleep(0.15)
    
    def alimentar(self):
        self.hambre -= random.randint(2,5)
        self.cansancio -= random.randint(2,3)
        self.animo += random.randint(1,2)

        alimentar1 = "\nMe estoy alimentando!\nÑam Ñam Ñam!\n"
        for letras in alimentar1:
            sys.stdout.write(letras)
            sys.stdout.flush()
            time.sleep(0.15)
    
    def jugar(self):
        self.animo += random.randint(3,5)
        self.fuerza -= random.randint(1,2)
        self.hambre += random.randint(2,4)

        jugar1 = "\nEstoy jugando!\nWeee!\n"
        for letras in jugar1:
            sys.stdout.write(letras)
            sys.stdout.flush()
            time.sleep(0.15)
    
    def dormir(self):
        self.hambre += random.randint(1,3)
        self.cansancio -= random.randint(3,5)
        self.fuerza += random.randint(1,2)

        dormir1 = "\nEstoy durmiendo!\nZZZzzz!\n"
        for letras in dormir1:
            sys.stdout.write(letras)
            sys.stdout.flush()
            time.sleep(0.15)
    
    def __str__(self):
        return (f"Tipo: {self.tipo}\nNombre: {self.nombre}\nFuerza: {self.fuerza}\nHambre: {self.hambre}\nÁnimo: {self.animo}\nCansancio: {self.cansancio}")


# Programa principal:

os.system("clear")
muerto = False
ciclo = 0
t = Tamagotchi("", 10, 10, 10, 10)
alias = "Ingrese el nombre de su mascota:\n"
for letras in alias:
            sys.stdout.write(letras)
            sys.stdout.flush()
            time.sleep(0.1)
t.nombre = input("> ").capitalize()

while muerto != True:
    os.system("clear")
    print(t)
    ciclo += 1
    
    accion = input("""
############################
#### Ingrese una acción ####
    
    [0] Tipos de mascotas
    [1] Ejercitar
    [2] Alimentar
    [3] Jugar
    [4] Dormir
    [5] Salir
############################
> """)
    
    while accion not in ["0", "1", "2", "3", "4", "5"]:
        os.system("clear")
        print(t)
        print("\nPor favor, ingrese una acción válida.")
        accion = input("""
############################
#### Ingrese una acción ####
    
    [0] Tipos de mascotas
    [1] Ejercitar
    [2] Alimentar
    [3] Jugar
    [4] Dormir
    [5] Salir
############################
> """)


    tiposMascota = """
Los tipos de animales sagrados nipones son:
-Genbu: Una tortuga con una serpiente
enrollada en el caparazón que representa
la tierra.
-Suzaku: Una majestuosa ave fénix que
representa el fuego.
-Byakko: Un tigre blanco símbolo del viento.
-Seiryu: Un dragón de color celeste cuyo
elemento es el agua.
"""
    terminar = "\nHas salido del juego!\n"

    if accion == "0":
        for letras in tiposMascota:
            sys.stdout.write(letras)
            sys.stdout.flush()
            time.sleep(0.1)
    elif accion == "1":
        t.ejercitar()
    elif accion == "2":
        t.alimentar()
    elif accion == "3":
        t.jugar()
    elif accion == "4":
        t.dormir()
    elif accion == "5":
        for letras in terminar:
            sys.stdout.write(letras)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.exit()

    if t.fuerza <= 0:
        muerto = True
    if t.animo <= 0:
        muerto = True
    if t.hambre >= 20:
        muerto = True
    if t.cansancio >= 20:
        muerto = True
    
final = f"""
############################
{t.nombre} ha muerto.
Vivió {ciclo} ciclos.
############################
"""
for letras in final:
            sys.stdout.write(letras)
            sys.stdout.flush()
            time.sleep(0.07)