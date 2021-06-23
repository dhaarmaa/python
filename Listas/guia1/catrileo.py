opcion = 0
notas = []
cont = 0
notas_ingresada = 0
while not opcion == "4":
    print("*****************************")
    print("SISTEMA DE CALIFICACIONES")
    print("*****************************")
    print("1)    AGREGAR NOTAS")
    print("2)    ELIMINAR NOTAS")
    print("3)    CALCULAR PROMEDIO")
    print("4)    SALIR")
    print("*****************************")
    opcion = input("INGRESE UNA OPCIÓN: ")

    if opcion == "1":
        if notas_ingresada >= 0:
            cont = 0
            for n in notas:
                print(f"{cont+1}) {n}")
                cont += 1

            if len(notas) == 0:
                print("NO HAY NOTAS REGISTRADAS")

            if len(notas) < 4:
                notas_ingresada = float(input("INGRESE NOTA: "))
                notas.append(notas_ingresada)
                print("LA NOTA HA SIDO REGISTRADA")
            if len(notas) >= 4:
                print("NO SE PERMITE INGRESAR MAS DE 4 NOTAS")
    elif opcion == "2":
        conta = 0
        print("NOTAS REGISTRADAS")
        for n in notas:
            print(f"{conta+1}) {n}")
            conta += 1
        print("INGRESE EL NUMERO DE LA NOTA QUE DESEA ELIMINAR: ")
        notas_eliminada = float(input())

        if notas_eliminada in notas:
            notas.remove(notas_eliminada)
            print("LA NOTA HA SIDO ELIMINADA")

        else:
            print("LA NOTA INGRESADA NO EXISTE")

    elif opcion == "3":

        if notas_ingresada > 0:
            contad = 0
            print("NOTAS REGISTRADAS")
            for n in notas:
                print(f"{contad + 1}) {n}")
                contad += 1
            resultado=notas
            promedio=sum(resultado)
            print(f"PROMEDIO DE NOTAS: {promedio/len(notas)}")
        else:
            print("NO HAY NOTAS REGISTRADAS")
    elif opcion == "4":
        print("HA SALIDO DEL SISTEMA DE NOTAS")
    else:
        print("LA OPCIÓN INGRESADA NO ES VÁLIDA")
