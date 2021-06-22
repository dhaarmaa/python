#●	Ingrese tres números enteros por teclado, súmelos e indique si la suma es mayor a 10.
import os
os.system("cls")
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))

calculo = num1+ num2 + num3

if calculo >=11:
    print(f"{calculo} es mayor a 10")
else:
    print(f"{calculo} es menor a 10")