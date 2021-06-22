import os 
os.system("cls")
#Ingrese un número entero y muestre su tabla de multiplicar
respuesta="s"
while respuesta=="s":
    num=int(input("Ingrese un numero:"))
    cont=1
    while cont<=10:
        multi=cont*num
        print(f"{num} por {cont} es: {multi}")
        cont+=1 
    respuesta=input("¿Desea volver a ejecutar? s/n:").lower()
print(f"FIN DEL PROGRAMA")