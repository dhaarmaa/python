import os
os.system('cls')

lado1 = int(input("ingrese el primer lado:"))
lado2 = int(input("ingrese el segundo lado:"))
lado3 = int(input("ingrese el tercer lado:"))
print("resultado")
if lado1==lado2 and lado1!=lado3 and lado2!=lado3:
    print("es un isoseles")
elif lado1!=lado2 and lado1!=lado3 and lado2!=lado3:
    print("es un triandulo escaleno")
else: 
    
    print("es un triangulo equilatero")