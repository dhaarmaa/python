import os
os.system("cls")
listTeam=[]
listScore=[]
def equipmentEntry():
    answer="si"
    while answer!="no":
        os.system("cls")
        name=input("Ingrese nombre de equipo:")
        score=int(input("Ingrese puntaje obtenido:"))
        listTeam.append(name)
        listScore.append(score)
        answer=input("¿Desea ingresar otro nombre si/no?").lower()
    for i in range(len(listTeam)):
        print(f"-{listTeam[i]} {listScore[i]}")
    #print(f"Puntaje es:{listScore[i]}")
def winningScore():
    higherScore=listScore[0]
    for i in range(len(listScore)):
        if listScore[i]>higherScore:
            higherScore=listScore[i]
    print(f" el equipo ganador es  {listTeam[i]} con {higherScore}")