#●	Ingrese un número e indique si es positivo o negativo.
import os
os.system('cls')
num = int(input("ingrese un numero: "))

if num<0:
    print(f"{num} es negativo")
else:
    print(f"{num} es positivo")