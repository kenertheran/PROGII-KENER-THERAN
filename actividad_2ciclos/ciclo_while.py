
print("menu: ")
print("1_persona")
print("2_vehiculo")
print("3_universidades")
print("4_notas")
print("5_salir")

while(True):
    
    opcion = int(input("ingrese un numero del 1 al 5_:"))

    if opcion == 1:
        print("usted a elegido la opcion personas")
        
    if opcion == 2:
        print("usted a elegido la opcion vehiculos")
        
    if opcion == 3:
        print("usted a elegido la opcion universidades")
        
    if opcion == 4:
        print("usted a elegido la opcion notas")
        
    if opcion == 5:
        print(SystemExit)
        break
    if opcion >=6:
        print("opcion invalida, por favor digite otra")



