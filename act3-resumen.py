import os
os.system('cls')

try:
    user = input("ingrese su nombre de usuario: ")
    password = input("ingrese su contraseña: ")
    if user== "pedro" and password == "1234" or user == "angel" and password == "a4s1":
        print("estas logueado puedes jugar")
        print("¿Cual de estas peliculas es de acción?\nA.Transformers\nB.Pasión de gavilanes\nC.IT\nD.El conjuro")
        resp1=input("Escoja la alternativa: ")
        print("\n¿cual de las siguientes peliculas es de terror?\nA.Amor a prueba\nB.split\nC.Son como niños\nD.Siempre alice")
        resp2=input("Escoja la alternativa: ")
        print("\n¿Cual de estas peliculas habla de viajes en el tiempo?\nA.El contador\nB.Proyecto almanaque\nC.Diario de una pasión\nD.Xmen")
        resp3=input("Escoja la alternativa: ")
        if resp1=="a" or resp1=="A":
            punt1=1.0
        else:   
            punt1=0
        if resp2=="B" or resp2=="b":
            punt2=1.0
        else:
            punt2=0
        if resp3=="b" or resp3=="B":
            punt3=1.0
        else:
            punt3=0
        punt_fin=punt1+punt2+punt3
        if punt_fin==1:
            print(f"\n**Obtuvo una respuesta buena**\nPuntaje: {punt_fin}\nNota: \"2.7\"")
        elif punt_fin==2:
            print(f"\n**Obtuvo dos respuestas buenas**\nPuntaje: {punt_fin}\nNota: \"4.5\"")
        elif punt_fin==0:
            print(f"\nNo obtuvo ninguna correcta :(\nPuntaje: {punt_fin}\nNota: \"1.0\"")
        else:
            print(f"\n**¡Felicidades! las obtuvo todas correctas** ^-^\nPuntaje: {punt_fin}\nNota: \"7.0\"")
    else: 
        print("usuario no valido")
except:
    print("respuesta invalida")

    
