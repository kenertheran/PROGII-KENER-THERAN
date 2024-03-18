vuelo = {
    "Areolinia": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "CTG",
    "Destino" : "MDE",
    "Tipo_de_Maleta": ['Cabina', 'Mano', 'Bodega']
    
}

print ("Valores del diccionario: ")
for key, value in vuelo.items():
    print(f"{key}: {value}")
    
print("\nValores de tipo maleta: ")
for maleta in vuelo ["Tipo_de_Maleta"]:
    print(maleta)