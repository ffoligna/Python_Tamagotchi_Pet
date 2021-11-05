num = int(input("""Ingrese un número positivo y entero
>_ """))


a = []
b = [] 

for i in range(0,num+1):
  a.append(i)

for j in range(0,num):
  b.append(j)

b.reverse()
c = a + b

print(c)