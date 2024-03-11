from datetime import datetime

class clientes:
    def __init__(self, cedula, nombre, apellido, telefono, correo, direccion, fecha_nacimiento):
        
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        
    def obtener_valores(self):
        return self.cedula, self.nombre, self.apellido, self.telefono, self.correo, self.direccion, self.fecha_nacimiento
    
    def calculo_de_edad(self):
        fecha_nacimiento = datetime.strptime(self.fecha_nacimiento,"%Y/%m/%d" ) 
        hoy = datetime.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad
    
cliente1 = clientes("1049582935", "Kener", "Theran", "3207478859", " kenersafat.theranrevolledo@unitecnar.edu.co", "Zaragocilla sector el progreso carrera 50A", "2006/4/11")

cedula, nombre, apellido, telefono, correo, direccion, fecha_nacimiento = cliente1.obtener_valores()

edad = cliente1.calculo_de_edad()

print(f"mi nombre es {nombre} {apellido} , vivo en {direccion} y tengo {edad} años.")
    
    
        
        