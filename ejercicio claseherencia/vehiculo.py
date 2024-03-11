class vehiculo:
    def __init__(self, fecha_fabricacion, VIN_chasis, VIN_motor):
        
        self.fecha_febricacion = fecha_fabricacion
        self.VIN_chasis = VIN_chasis
        self.VIN_motor = VIN_motor
        
    def obtener_fecha_fabricacion(self):
        return self.fecha_febricacion
    
    def obtener_VIN_chasis(self):
        return self.VIN_chasis
    
    def obtener_VIN_motor(self):
        return self.VIN_motor
    
class automovil (vehiculo):
    def __init__(self, fecha_fabricacion, VIN_chasis, VIN_motor, marca, modelo, precio):
        super().__init__(fecha_fabricacion, VIN_chasis, VIN_motor)
        
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        
    def obtener_marca(self):
        return self.marca
    
    def obtener_modelo(self):
        return self.modelo
    
    def obtener_precio(self):
        return self.precio
    
    def mostrar_datos(self):
        messaje = f"la marca de este automovil es {self.marca} y su modelo es {self.modelo} , el cual fue fabricado en el año {self.fecha_febricacion}. "
        messaje += f"Su VIN de chasis es {self.VIN_chasis}, y su VIN de motor es {self.VIN_motor}. "
        messaje += f"Su precio es de {self.precio} dolares." 
        print(messaje)
        
auto1 = automovil("2023", "KS2006", "TR114", "Mercedes", "AMG CLA 45S 4MATIC", 94500)

auto1.mostrar_datos()
         
        