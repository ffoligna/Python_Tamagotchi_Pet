# Ejercicio "Mad Libs" o "Escoge tu propia historia"

print("----------------------------")
print("Mad Libs o Escoge la Palabra")
print("----------------------------")
print("")

while True:
    try:
        time_a = int(input("Introduce un numero entero: "))
        break
    except ValueError:
        print('Error, introduce un numero entero')

body_part = input("Una parte del cuerpo: ")
food = input("Un alimento: ")

educative_centre = input("Escriba una de las opciones (E para Escuela o U para Universidad): ")

while (educative_centre !="E" and educative_centre !="U"):
    print("Error!, escriba una de las opciones (E para Escuela o U para Universidad): ")
    educative_centre = input("Escriba una de las opciones (E para Escuela o U para Universidad): ")
    
if educative_centre == "E":
    educative_centre = "Escuela"
if educative_centre == "U":
    educative_centre = "Universidad"

lesson_01 = input("Una materia educativa: ")
lesson_02 = input("Otra materia educativa: ")

lesson_01 = lesson_01.capitalize()
lesson_02 = lesson_02.capitalize()

while (lesson_02 == lesson_01):
    print("Error, ingrese una distinta a la primera")
    lesson_02 = input("Otra materia educativa: ")
    lesson_02 = lesson_02.capitalize()

hobby = input("Un hobby o actividad: ")

while True:
    try:
        time_b = int(input("Introduce un numero entero: "))
        break
    except ValueError:
        print('Error, introduce un numero entero')

mourning_task = input("Algo que haces todas las mañanas: ")

electric_device = input("Escribir una de las opciones (Celular, Tablet o Notebook): ")

while (electric_device !="C" and electric_device !="T" and electric_device !="N"):
    print("Error!, escriba una de las opciones (C para Celular, T para Tablet o N para Notebook): ")
    electric_device = input("Escriba una de las opciones (C para Celular, T para Tablet o N para Notebook): ")

if electric_device == "C":
    electric_device = "Celular"
if electric_device == "T":
    electric_device = "Tablet"
if electric_device == "N":
    electric_device = "Notebook"

adjetive = input("Un adjetvio en plural: ")
home_task = input("Algo que haces en casa (verbo en tiempo presente): ")
outside_task = input("Algo que haces fuera de casa: ")
name = input("Un nombre: ")

while True:
    try:
        month = int(input("Un mes del año en formato numérico: (1 a 12) "))
        while (month < 1 or month > 12):
            month = int(input("Error, ingrese un mes del año en formato numérico: (1 a 12) "))
        break
    except ValueError:
        print('Error, introduce un numero entero ')


print("")
print("--------------------")
print("Tu historia Mad Libs")
print("********************")
print("")

print(f"Antes del Coronavirus, me levantaba a las {time_a}")
print(f"Me bañaba, cepillaba mi/s {body_part} y comía {food} de desayuno.")
print(f"Iba a la {educative_centre} a las 8:30 a.m.")
print(f"Mi materia preferida es {lesson_01}, pero no me gusta {lesson_02}.")
print(f"Después de la {educative_centre}, {hobby} y me iba a dormir a las {time_b}.")
print(f"Ahora, {mourning_task} a las 9 a.m. Tengo clases virtuales en mi {electric_device}.")
print(f"Me gustan las clases virtuales, pero a veces son {adjetive}.")
print(f"Tengo mucho tiempo libre y a veces {home_task},")
print(f"pero no puedo salir y {outside_task}.")
print(f"De vez en cuando hago video llamadas con mi mejor amigo, {name}.")
print("No me molesta quedarme en casa,")
print(f"pero quiero que termine la cuarentena en {month}.")
