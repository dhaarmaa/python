
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
        print("No es palindromo")

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
