#Ingresados dos números por el usuario, este programa nos muestra el valor mayor o si son iguales.

a = int(input("Ingrese el valor A: "))
b = int(input("Ingrese el valor B: "))

if (a==b):
    print ("Los valores son iguales.")
    
else:
    if (a>b):
        print ("El mayor es A =", a)
    else:
        print ("El mayor es B =", b)