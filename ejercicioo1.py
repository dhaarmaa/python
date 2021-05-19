#una tienda de helados ofrece 3 tipos :
#vaso pequeño $1000, vaso mediano $2000 y vaso grande $3500
#opcionalmente puede agregar: 
#frutas a 500 o chocolate a 600
#ppor otra parte puede añadir salsa de chocolate o frutilla a 200 o bien manjar a 300. 
#arrojar los productor  seleccionados , en total a pagar (segun eleccioón ), ingresar el dinero y mostrar vuelto 

import os
os.system('cls')
try:
    print("BIENVENIDO\n ¿Qué tipo de vaso desea llevar?\n 1)pequeño $1000\n 2)mediano $2000\n 3)grande $3500")
    cup = int(input("por favor ingrese su elección: "))

    if cup == 1:
        typeCup = " pequeño"
        cost = 1000
    elif cup == 2:
        typeCup = "mediano"
        cost = 2000
    elif cup == 3:
        typeCup = "grande"
        cost = 3500
    else:
        print("por favor ingrese una respuesta valida")

    print("Desea agregar:\n 1)fruta $500 \n 2)chocolate $600\n 3) ninguno")
    optionalAddition = int(input("ingrese su elección: "))

    if optionalAddition == 1:
        addition = "fruta"
        costAddition = 500
    elif optionalAddition == 2:
        addition = "chocolate"
        costAddition = 600
    elif optionalAddition == 3:
        addition="ninguna"
        costAddition = 0
    else:
        print("por favor ingrese una respuesta que este dentro de las opciones")

    print("Desea agregar algun tipo de salsa: \n 1)chocolate $200\n 2)Frutilla $200\n 3)manjar $300 \n 4)ninguna")
    sauce = int(input(" ingrese su elección: "))

    if sauce == 1:
        typeSauce = "chocolate"
        costSauce = 200
    elif sauce == 2:
        typeSauce = "frutilla"
        costSauce = 200
    elif sauce == 3:
        typeSauce = "manjar"
        costSauce = 300
    elif sauce == 4:
        typeSauce = "ninguna"
        costSauce= 0
    else:
        print("por favor ingrese una elección valida")

    totalToPay = cost+costAddition+costSauce

    print( f"El total a pagar es {totalToPay} ")
    moneyEntered = int(input("por favor ingrese el monto con el que va a pagar: "))

    if totalToPay == moneyEntered:
        change = 0
    elif totalToPay > moneyEntered:
        print("por favor ingrese la misma cantidad o una mayor para pagar: ")
    else:
        change =  moneyEntered - totalToPay

    print("\n\n\n****RESUMEN DE COMPRA******")
    print(f"tipo de vaso: {typeCup}")
    print(f"valor: {cost}")
    print(f"añadido opcional: {addition}")
    print(f"valor: {costAddition}")
    print(f"tipo de salsa: {typeSauce}")
    print(f"valor: {costSauce}")
    print(f"total a pagar: {totalToPay}")
    print(f"total con lo que paga: {moneyEntered}")
    print(f"vuelto: {change}")
    print("GRACIAS POR SU COMPRA :)")
except:
    print("me vale esto")
2