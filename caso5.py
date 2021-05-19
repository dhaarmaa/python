#	Ingrese un número entero e indique si es par o impar.
import os
os.system

num = int(input("ingrese un número: "))

calculo = num%2

if calculo==0:
    print(f"{num} es par")
else:
    print(f"{num} es impar")