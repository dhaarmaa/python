import os
from typing import ChainMap 
os.system('cls')

try:
    print("BIENVENIDO")
    print("que hamburguesa desea agregar: ")
    print(" 1) Hamburguesa queso $2000 \n 2) Hamburguesa con tocino $2500 \n 3) Hamburguesa doble especial $3000")
    hamburguesa = int(input("que hamburguesa desea llevar: "))
    if hamburguesa == 1:
        tipoHamburguesa = "hamburguesa queso"
        costo = 2000
    elif hamburguesa == 2:
        tipoHamburguesa = "Hamburguesa  con tocino"
        costo = 2500
    elif hamburguesa ==3:
        tipoHamburguesa = "Hamburguesa doble especial"
        costo = 3000
    else:
        print("Respuesta invalida")

    print("Desea alguna bebida \n 1) Bebida normal $500 \n 2) Bebida grande $1000 \n 3) jugo néctar $1000")
    bebida = int(input("elija su opción: "))
    if bebida ==1:
        tipoBebida = "normal"
        costoBebida = 500
    elif bebida == 2:
        tipoBebida = "grande"
        costoBebida = 1000
    elif bebida == 3:
        tipoBebida =  "jugo néctar"
        costoBebida = 1000
    else:
        print("Respuesta invalida")
    
    print("Agregados: \n 1) Papas fritas $600 \n 2) Porción 2 empenadas queso $500 \n 3) Porción de 4 empanadas queso $900 \n 4)ningun agregado")
    agregados = int(input("cual desea agregar: "))
    if agregados ==1:
        tipoAgregado = " Papas fritas"
        costoAgregado = 600
    elif agregados ==2:
        tipoAgregado = "Porción 2 empanadas queso"
        costoAgregado = 500
    elif agregados ==3:
        tipoAgregado = " Porción de 4 empanadas queso"
        costoAgregado = 900
    elif agregados ==4:
        tipoAgregado ="ningun agregado"
        costoAgregado =  0
    else:
        print("Respuesta invalida")
    
    print("Que postre desea agregar: \n 1) Vaso helado $300 \n 2) Fruta a elección $200 \n 3) ningun postre")
    postre = int(input("ingrese su elección: "))
    if postre ==1:
        tipoPostre = "Vaso de helado"
        costoPostre = 300
    elif postre ==2:
        tipoPostre = "Fruta a eleciión"
        costoPostre = 200
    elif postre == 3:
        tipoPostre  = "Ningun postre"
        costoPostre = 0
    else:
        print("Respuesta invalida")
    
    total = costo + costoAgregado + costoPostre
    print("Que tipo de Cliente es: \n 1) Estudiante becado \n 2) Profesor \n 3) Administrativo \n 4)otro")
    cliente = int(input("ingrese su elección"))
    if cliente ==1:
        tipoCliente = "Estudiante becado"
        porcentaje ="60%"
        calculoDcto = (total*60)/100
        Descuento = total - calculoDcto
    elif cliente ==2:
        tipoCliente = "profesor"
        porcentaje ="40%"
        calculoDcto = (total*40)/100
        Descuento = total - calculoDcto
    elif cliente ==3:
        tipoCliente = "Administrativo"
        porcentaje ="100%"
        Descuento = total-total
    elif cliente ==4:
        tipoCliente = "otro"
        porcentaje = "0"
        calculoDcto =0
        Descuento = total
    else:
        print("Respuesta invalidad")
    print(f"total: {total}")

    dineroIngresado =int(input("ingrese el dinero con el que va a pagar"))
    if dineroIngresado >= 0:
        vuelto = dineroIngresado -Descuento
    
    else:
        print("Dinero insuficiente para el pago")



    print("**********RESUMEN DE COMPRA***********")
    print(f"Tipo de hamburguesa: {tipoHamburguesa}")
    print(f"costo: ${costo}")
    print(f"Tipo de bedida: {tipoBebida}")
    print(f"costo: ${costoBebida}")
    print(f"Agregado: {tipoAgregado}")
    print(f"costo: ${costoAgregado}")
    print(f"tipo de postre: {tipoPostre}")
    print(f"costo: ${costoPostre}")
    print(f"total: ${total}")
    print(f"tipo de cliente: {tipoCliente}")
    print(f"Descuento aplicado: {porcentaje}")
    print(f"total a pagar: ${Descuento}")
    print(f"dinsero ingresado: ${dineroIngresado}")
    print(f"vuelto: ${vuelto}")
    print("************gracias!***********")
except:
    print("fin del programa")