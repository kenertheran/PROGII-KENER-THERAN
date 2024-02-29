class estudiante:
    def __init__(self, nombre, apellido, cedulaint, correo, telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.cedulaint=cedulaint
        self.correo=correo
        self.telefono=telefono
        
        
    def obtenernombre(self):
        return f'mi nombre es {self.nombre} {self.apellido}'

    def obtenercedula(self):
        return f'mi cedula es {self.cedulaint}'

    def obtenercorreo(self):
        return f'mi correo es {self.correo}'

    def obtenertelefono(self):
        return f'y mi telefono es {self.telefono}'
 
p=estudiante("kener", "theran", "1049582935", "kenersafattheran@gmail.com", "3207478859")

print(p.obtenernombre(), p.obtenercedula(), p.obtenercorreo(), p.obtenertelefono())
 
    

