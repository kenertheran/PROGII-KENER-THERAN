it_companies =['Facebook', 'Google', 'Micosoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#funcion insertar
it_companies.insert(0, 'Asus')

print(it_companies)
#comprobar si existe una empresa
existe_o_no = "Facebook" in it_companies
print(existe_o_no)

#ordenar la lista con el metodo sort()
it_companies.sort()
print(it_companies)

#Invierte la lista en orden descendente utilizando el método reverse()
it_companies.sort(reverse= True)
print(it_companies)

#Elimine la primera empresa informática de la lista utilizando el metodo pop y delete
it_companies.pop(0)
print(it_companies)

del it_companies[0]
print(it_companies)

#Eliminar todas las empresas de la lista it_companies
it_companies.clear()
print(it_companies)






