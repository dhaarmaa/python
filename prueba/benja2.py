import os
os.system ('cls')

print(" !Hola, bienvenido !")
print("¿Que Hamburgesa desea?")
print("1.-Hamburgesa de queso $2000 c/u \ 2.-Hamburgesa con tocino $2500 c/u \ 3.-Hamburgesa doble especial $3000 c/u \ 4.- Ninguna Hamburgesa")
opcion=int(input("Escoja una de las anteriores:"))
if opcion==1:
    precio = 2000
    hamburgesa = "Hamburgesa con queso"
elif opcion==2:
    precio = 2500
    hamburgesa = "Hamburgesa con tocino"
elif opcion==3:
    precio = 3000
    hamburgesa = "Hamburgesa doble especial"
elif opcion==4:
    precio = 0

print("----- Bebidas -----")
print("1.-Bebida normal $500 c/u \ 2.-Bebida grande $1000 c/u \ 3.-Jugo de Nectar $1000 c/u \ 4.- Ninguna bebida")
opcion = int(input("escoja una bebida:"))
if opcion==1:
    precio+= 500
    bebida = "Bebida normal"
elif opcion==2:
    precio=+ 1000
    bebida = "Bebida grande"
elif opcion==3:
    precio+= 1000
    bebida = "Jugo de nectar"
elif opcion==4:
    precio = 0

print("----- Agregados -----")
print("1.-Papas Fritas $600 c/p \ 2.- 2 Empanadas de queso $500 c/u \ 3.- 4 Empanadas de queso $900 c/u \ 4.- Ningun agregado")
opcion=int(input("Escoja un tipo de agregado:"))

if opcion==1:
    precio+= 600
    agregado = "Papas fritas"
elif opcion==2:
    precio+= 500
    agregado = "2 Empanadas de queso"
elif opcion==3:
    precio=+ 900
    agregado = "4 Empanadas de queso"
elif opcion==4:
    precio=0

print("----- Postres -----")
print("1.- Vaso de helado $300 c/u \ 2.- Fruta a eleccion $200 c/u \ 3.- Ningun postre")
opcion=int(input("Escoja un tipo de postre:"))

if opcion==1:
    precio+= 300
    postre = "Vaso de helado"
elif opcion==2:
    precio+= 200
    postre = "Fruta a eleccion"
elif opcion==3:
    precio=0

print("----- Descuentos -----")
print("¿Que tipo de cliente es usted")
print("1.- Estudiante becado \ 2.- Profesor \ 3.- Administrador \ 4.- Cliente normal")
cliente = int(input("Seleccione que tipo de cliente es usted:"))
if cliente==1:
    tipo_cliente = "Estudiante becado"
    des=0.60
elif cliente==2:
    tipo_cliente = "Profesor"
    des=0.40
elif cliente==3:
    tipo_cliente = "Administrador"
    des=1
elif cliente==4:
    tipo_cliente = "Cliente normal"
    des=0
else:
    print("error de sistema")

print(f"El total de la compra es:{precio-(precio*des)}")
dinero=int(input("Ingrese el dinero con el que cancelara: "))
calculo = precio-(precio*des)
if dinero>=calculo:
    vuelto= dinero -calculo

    print(f"Detalle: Usted escojio: {hamburgesa},{bebida},{agregado},{postre} y {tipo_cliente}")
    print(f"Su descuento es de: ${des}")
    print(f"Usted pago con: ${dinero}")
    print(f"Su vuelto es de: ${vuelto}")
else:
    print("dinero insuficiente")