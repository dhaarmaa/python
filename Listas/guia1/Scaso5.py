import os
os.system('cls')
list =[]
print("1)en \n2)feb \n3)mar \n4)abr \n5)may \n6)jun \n7)jul \n8)agost \n9)sept \n10)oct \n11)nov \n12)dic")

month = int(input("ingre mes: "))
while month<1 or month>12:
    month= int(input("Ingrese número de mes correcto: "))
#separamos los meses que tiene 31 dias 
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==12:
    execute = True    
    for i in range(31):
        execute = True
        while execute:
            try:
                dollar = float(input(f"Ingrese valor del día {i}"))
                list.append(dollar)
                i+= 1
                execute = False
            except:
                print("error al ingreso")
                execute = True
elif month == 4 or  month == 6 or month == 9 or month ==11:
    execute = True    
    for i in range(30):
        execute = True
        while execute:
            try:
                dollar = float(input(f"Ingrese valor del día {i}"))
                list.append(dollar)
                i+= 1
                execute = False
            except:
                print("error al ingreso")
                execute = True
  
elif month ==2:
    execute = True    
    for i in range(28):
        execute = True
        while execute:
            try:
                dollar = float(input(f"Ingrese valor del día {i}"))
                list.append(dollar)
                i+= 1
                execute = False
            except:
                print("error al ingreso")
                execute = True
for i in range(len(list)):
   
     print(f"valor del dolar en el día es {i+1} es: {list[i]}")
smaller = list[0]
higher = list[0]
daySmaller = 1
dayHigher = 2
for i in range(30):
    if list[i] > higher:
        dayHigher = i+1
        higher = list[i]
    if list[i] < smaller:
        daySmaller = i+1
        smaller = list[i]          
print(f"Mayor alza del dolar fue de:{higher} el día {dayHigher}")
print(f"Mayor alza del dolar fue de:{smaller} el día {daySmaller}")
