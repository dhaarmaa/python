#Una bencinera ofrece distintos tipos de servicio que un cliente puede tomar que serían los siguientes: 
# cargar combustible: bencina 900 el litro o diésel 600 el litro, puede cargar varios litros de un tipo de combustible.
# Otro servicio es el de limpieza donde la ficha de hidrolavadora puede costar 1500 por 2 minutos o 2500 por 3 minutos. Finalmente puede aspirar el vehículo zadquiriendo una ficha por 1200 pesos. Hay que señalar que cualquiera de estos servicios es opcional. Al finalizar arroje el detalle de todos los servicios adquiridos, total a cancelar, dinero a pagar y vuelto. Considere mensajes en caso de no seleccionar una opción válida. 
import os
os.system('cls')
try:

    print("BIENVENiDOS \n Valor de la combustible: \n  1)Bencina a 900 el litro \n  2)Diesel 600 el litro")

    fuelType = int(input("ingrese su elección: "))
    fuelQuantity = int(input("ingrese la cantidad que quiere: "))

    if fuelType == 1:
        fuel = "Bencina"
        cost = 900
        fuelCost = fuelQuantity*900
    elif fuelType == 2:
        fuel = "Diesel"
        cost = 600
        fuelCost = fuelQuantity * 600
    else:
        print("opción invalida")

    print("limpieza desde ficha de hidrolavadora \n 1)2 minutos a 1500 \n 3 minutos a 2500 \n 3)ninguno")
    cleaning = int(input("Ingrese su elección"))

    if cleaning == 1:
        typeCleaning = "2 minutos"
        costCleaning = 1500
    elif cleaning == 2:
        typeCleaning = "3 minutos"
        costCleaning = 2500
    elif cleaning == 3:
        typeCleaning = "ningun minuto"
        costCleaning = 0
    else:
        print("respuesta invalida")
    print("desea el servicio de aspirar su auto: \n 1) sí \n 2) No")
    carAspire = int(input("ingrese su respuesta: "))
    if carAspire == 1:
        costAspire = 1200
        aspire = "si"
    elif carAspire == 2:
        costAspire = 0
        aspire = "no"
    else:
        print("respuesta invalida")
    total = cost + costCleaning + costAspire
    print(f"el total es {total}")
    money = int(input("ingrese dinero"))
    if money > total:
        change = money-total
    elif money == total:
        change = 0
    else:
        print("ingrese un monto mayor al total")

    print("***********RESUMEN DE COMPRA**************")
    print(f" tipo de combustible: {fuel}")
    print(f"litros: {fuelQuantity}")
    print(f"costo: {cost}")
    print(f"limpieza por {typeCleaning}")
    print(f"costo: {costCleaning}")
    print(f"aspirada de auto : {aspire}")
    print(f"costo: {costAspire}")
    print(f"total de venta: {total}")
    print(f"dinero ingresado: {money}")
    print(f"vuelto: {change}")
    print("\n *****GRACIAS POR PREFERIRNOS*****")

except:
    print("respuesta invalida")
