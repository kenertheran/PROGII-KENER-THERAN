#diccionario vacio
diccionario_perro= {}

#diccionario perro
diccionario_perro= {
    'nombre': "princesa",
    'color': "cafe claro",
    'raza': "pitbull",
    'patas': " 4",
    'edad': "5 años"
    
}
print(diccionario_perro)

#diccionario estudiante
diccionario_estudiante= {
    'nombre': "kener",
    'apellido': "theran",
    'sexo': "masculino",
    'edad': "17 años",
    'estado civil': "soltero",
    'habilidades': ['aprendo rapido','soy muy puntual'],
    'pais': "colombia",
    'ciudad': "cartagena",
    'direccion': "zaragocila Cra 50A"
    
    
}
print(diccionario_estudiante)
print(len(diccionario_estudiante))
#obtener el valor de habilidades y comprobar el tipo de dato
print(type(diccionario_estudiante['habilidades'])) 

#modificar los valores de las habilidades
diccionario_estudiante['habilidades'].append('liderar')
diccionario_estudiante['habilidades'].append('trabajo en equipo')
print(diccionario_estudiante['habilidades'])

#obtener claves de un diccionario como una lista
keys = diccionario_estudiante.keys()
print(keys)

#obtener los valores del diccionario como una lista
valores= diccionario_estudiante.values()
print(valores)

#Cambie el diccionario a una lista de tuplas utilizando el método items()
print(diccionario_estudiante.items())

#Eliminar uno de los elementos del diccionario
diccionario_estudiante.pop('habilidades')
print(diccionario_estudiante)

#Borrar uno de los diccionarios
print(diccionario_perro)
print(diccionario_perro.clear())