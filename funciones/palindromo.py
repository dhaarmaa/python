#ngrese un número entero máximo de 3 dígitos, luego indique:
#● Si es un Palíndromo (es un número que se lee igual en un sentido que en otro)
#● Separe los dígitos y muestre en forma vertical
#● *Usar funciones.

		
	
#palindromo()
import os 
os.system('cls')

def calculo(number):
    resultado = number//10
    resto1= number%10
    print(resto1)
    resto2 = resultado%10
    print(resto2)
    resto3 =  resultado//10
    print(resto3)
    if resto1 == resto3:
        print("es palindromo")
    else:
        print("NO LO ES")

def palindromo():
    answer = "s"
    while answer != "n":

        number = int(input("ingrese numero: "))
        if number >=100 and number <= 999:
            calculo(number)
            
        else:
            print("NUMERO INVALIDO.")

    answer = input("desea revisar otro numero? s/n")
palindromo()


#OTRA FORMA
import os
os.system('cls')

def palindromo():
    number = input("ingresse un numero: ")
    rev = number[::-1]
    if number == rev:
        print("es palindromo")
        
    else:
        print("no lo es")

palindromo()
