#●	Ingrese tres números enteros e indique cuál de ellos es menor.
import os #el os es para acceder en el sistema
os.system('cls') #es para limpiar la terminal
num1 = int(input("ingrese primer numero: "))
num2 = int(input("ingrese segundo numero: "))
num3 = int(input("ingrese tercer numero: "))
if num1<num2 and num1<num3:
    print(f"{num1} es el menor")
elif num2<num1 and num2<num3:
    print(f"{num2} es el menor")
else: 
    #num3>num1 and num3>num2
    print(f"{num3} es el menor")
print("fin de l proceso...")