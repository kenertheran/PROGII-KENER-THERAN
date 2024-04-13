# parcial 2 corte: kener safat theran revolledo y fabian andres perez melendez

# creamos la clase persona
class Personas:
    
    def __init__(self) :
        global user  # crea una variable global cuyo valor se pude modificar
        user = []
# definimos el primer menu
    def menu_1(self):
        while True:
            # mandamos a imprimr el menu de personas
            print("\n Menu personas")
            print("1. crear")
            print("2. listar")
            print("3. actualizar")
            print("4. eliminar")
            print("5. volver al menu principal") 
# mandamos al usuario a selecionar una opcion 
            opcion = input("seleccione una opcion: ")

            if opcion == "1":
                print(Personas.crear())
            elif opcion == "2":
                print(Personas.listar())
            elif opcion == "3":
                print(Personas.actualizar()) 
            elif opcion == "4":
                print(Personas.eliminar())
            elif opcion == "5":
                break   
        
            else:
                print("opcion invalida, por favor digite otra opcion.")
# definimos la opcion crear 
    def crear():
        print('haz seleccionado la opcion crear')
        
        per = input("ingrese a una persona: ")
        ide = input('ingrese el numero de identificacion de la persona: ')
        gen = input('ingrese el genero de la persona: ')
        eda = input('ingrese la edad de la persona: ')
        cel = input('ingrese el numero celular de la persona: ')
        # agregar elemento a una lista
        user.append(per)
        user.append(ide)
        user.append(gen)
        user.append(eda)
        user.append(cel)
        
        
        return f'agregar el dato',per,ide,gen,eda,cel

# definimos la opcion listar
    def listar():
        print("haz seleccionado la opcion listar")

        return f'los datos que estan hasta ahora son',user
# definimos la opcion actualizar
    def actualizar():
        print("haz seleccionado la opcion actualizar")
        posicion =int(input("ingrese la opcion del tado el cual se va a actualizar: "))

        if 0 <= posicion < len(user):
            cambio = input("ingrese el nuevo dato por el cual se va a actualizar: ")
            user[posicion] = cambio

            return f'se han actualizado los datos del usuario', posicion,'la actual lista de datos es: ',user

        else:

            return "la posicion del dato es invalida"
# definimos la opcion eliminar
    def eliminar():
        print("haz seleccionado la opcion eliminar")

        eliminar = input("ingrese el dato, al cual desea eliminar: ")
        user.remove(eliminar)

        return f'el usuario al cual usded a eliminado es',eliminar, 'la actual lista de usiarios es', user




# creamos la clase universidades
class Universidades:
    
    def __init__(self) :
        global user
        user= []
        # definimos el segundo menu
    def menu_2 (self):
        while True:
            # mandamos a imprimir el menu de universidades
            print("\n Menu Universidades")
            print("1. crear" )      
            print("2. listar")
            print("3. actualizar")
            print("4. eliminar")
            print("5. volver al menú principal")
# mandamos al usuario a selecionar una opcion 
            opcion = input("Por favor, seleccione una opcion: ")
            
            if opcion == "1":
                print(Universidades.Crear())
        
            elif opcion == "2":
                print(Universidades.Listar())
        
            elif opcion == "3":
                print(Universidades.Actualizar())
                
            elif opcion == "4":
                print(Universidades.Eliminar())        
                
            elif opcion == "5":
                break


            else:
                print("Opcion invalida, por favor digite otra opcion.")
# definimos la opcion crear 
    def Crear():
        print("haz seleccionado la opcion crear")
        uni = input("ingrese la universidad: ")
        rec = input('ingrese el rector de la universidad')
        dir = input('ingrese la direccion de la universidad')
        
        user.append(uni)
        user.append(rec)
        user.append(dir)
        
        
        return f'queda el dato agregado',uni,rec,dir

# definimos la opcion listar
    def Listar():
        print("haz seleccionado la opcion listar")

        return f'los datos que estan hasta ahora son: ',user

# definimos la opcion actualizar
    def Actualizar():
        print  ("haz seleccionado la opcion actualizar")
        posicion = int(input("ingrese el nuevo dato por el cual se va a actualizar: "))
        if 0 <= posicion < len(user):
            cambio = input("Ingrese el cambio de nombre de la universidad: ")
            user[posicion] = cambio
            return f'Se actualizada los datos de la universidad' ,posicion , 'La lista actual es: ', user
        # definimos la opcion eliminar
    def Eliminar():
            print("haz seleccionado la opcion eliminar")
            eliminar = input("ingrese la universidad que desea eliminar: ")
            user.remove(eliminar)

            return f'la universidad la cual usded a eliminado es',eliminar, 'la actual lista de universidades es', user



# creamos la clase Notas
class Notas:
    def __init__(self): 
            global user
            user= []
# definimos el tercer menu
    def menu_3 (self):        
        while True:
# mandamos a imprimir el menu de notas
            print("\nMenu De Notas")
            print("1. crear")
            print("2. listar")
            print("3. actualizar")
            print("4. eliminar")
            print("5. volver al menú principal")
            # mandamos al usuario a selecionar una opcion  
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Notas.Crear())
            elif opcion == "2":
                print(Notas.Listar())
            elif opcion == "3":
                print(Notas.Actualizar())
            elif opcion == "4":
                print(Notas.Eliminar())
            elif opcion == "5":
                break
            
            else:
                print("Opción inválida, por favor digite otra opcion.")
    # definimos la opcion crear
    def Crear():
        print ('haz seleccionado la opcion crear')
        
        mat = input("ingrese la materia: ")
        nota = input("ingrese la nota")
    
        user.append(mat)
        user.append(nota)
        
        
        return f'Usted ha agregado el dato',mat,nota
    
    # definimos la opcion listar
    def Listar():   
        print("haz seleccionado la opcion listar")
        
        return f'los datos de nuestra base son',user
    # definimos la opcion actualizar
    def Actualizar():
        print("haz seleccionado la opcion actualizar")
        posicion = int(input("Ingrese la posición de el dato a actualizar: "))
        if 0 <= posicion < len(user):
            cambio = input("Ingrese el cambio de dato: ")
            user[posicion] = cambio
            
            return f'Se han actualizado los datos de la nota' ,posicion , 'La lista actual es: ', user
        else:
            
            return "La posición que ha ingresado no es valida."
    # definimos la opcion eliminar
    def Eliminar():
        print("haz seleccionado la opcion eliminar")
        eliminar=input("ingrese el dato a eliminar: ")
        user.remove(eliminar)
        
        return f'la nota que ha sido eliminada es',eliminar,'la lista actual es', user



# Creamos la clase asignaturas
class Asignaturas:
    
    def __init__(self):
        global user
        user = []
    
    # definimos el cuarto menu
    def menu_4(self):
        while True:
            # mandamos a imprimir el menu de asignaturas
            print("\nMenu De Asignaturas")
            print("1. crear")
            print("2. listar")
            print("3. actualizar")
            print("4. eliminar")
            print("5. volver al menú principal")
            # mandamos al usuario a selecionar una opcion  
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print(Asignaturas.Crear())
            elif opcion == "2":
                print(Asignaturas.Listar())
            elif opcion == "3":
                print(Asignaturas.Actualizar())
            elif opcion == "4":
                print(Asignaturas.Eliminar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida, por favor digite otra opcion.")
    # definimos la opcion crear
    def Crear():
        print ('haz seleccionado la opcion crear')
        asig = input("ingrese la asignatura: ")
        prof = input("ingrese el profesor el cual pertenece a la asignatuara: ")
        cre = input("ingrese los creditos de la signatura: ")
        
        user.append(asig)
        user.append(prof)
        user.append(cre)
        
        return f'Usted ha agregado el dato',asig,prof,cre
    # definimos la opcion listar
    def Listar():   
        print("haz seleccionado la opcion listar")
        
        return f'los datos de nuestra base son',user
    # definimos la opcion actualizar
    def Actualizar():
        print("haz seleccionado la opcion actualizar")
        posicion = int(input("Ingrese la posición del dato a actualizar: "))
        if 0 <= posicion < len(user):
            cambio = input("Ingrese el cambio de dato: ")
            user[posicion] = cambio
            
            return f'Se han actualizado los datos de la asignatura' ,posicion , 'La lista actual es: ', user
        
        else:
            
            return "La posición que ha ingresado no es valida."
    # definimos la opcion eliminar
    def Eliminar():
        print("haz seleccionado la opcion eliminar")
        eliminar=input("ingrese el dato a eliminar a eliminar: ")
        user.remove(eliminar)
        
        return f'la asignatura que ha sido eliminada es',eliminar,'la lista actual es', user
        

# definimos el menu principal
def Menu():
    while True:
        # mandamos a imprimir el menu principal
        print("\n Menu Principal:")
        print("1. Personas")
        print("2. Universidades")
        print("3. Notas")
        print("4. Asignatura")
        print("5. salir")
        # mandamos al usuario a selecionar una opcion  
        opcion= input("Seleccione una opcion: ")
            
        if opcion == "1":
            m = Personas()
            m.menu_1()
            
        elif opcion == '2':
            u = Universidades()
            u.menu_2()
            
        elif opcion == '3':
            n = Notas()
            n.menu_3()
            
        elif opcion == '4':
            a = Asignaturas()
            a.menu_4()
            
        elif opcion == '5':
            print("ha saliso del Menu")
            break
        
        else:
            print("Opcion invalida, por favor digite otra opcion")
Menu()
