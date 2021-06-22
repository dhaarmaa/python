#●	Ingrese tres números, indique cuántos de ellos son positivos.

import os
os.system('cls')
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero"))
num3 = int(input("ingrese el tercer numero"))

if num1>0 and num2>0 and num3>0:
    print(f"{num1}, {num2} y {num3} son positivos")
elif num1>0 and num2>0 and num3<0:
    print(f"{num1} y {num2}  son positivos")
elif num1>0 and num2<0 and num3>0:
    print(f"{num1} y {num3}  son positivos")
elif num1>0 and num2<0 and num3<0:
    print(f"{num2} y {num3}  son positivos")

else:
    print("ninguno es positivo")