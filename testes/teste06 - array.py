#Trabalhando com Array (Lista)
lista1 = ["a","b","c","d","e","f","g"] #Uma lista de String
lista2 = [1,2,3,4,5,6,7,8,9] #Uma lista de Ints
lista3 = ["a",1,"abc",2.5,"xyz",True,2+2] #Uma lista mista

#Exibindo as listas
print(f"Lista 1 (String): {lista1}")
print(f"Lista 2 (Int): {lista2}")
print(f"Lista 3 (Mista): {lista3}")

#Exibindo um item especifico da lista através de sua index
print(f"Item 1 da Lista 1: {lista1[0]}")
print(f"Item 5 da Lista 2: {lista2[4]}")
print(f"Item Aleatório da Lista: {lista3[5]}")

#Substituindo valor de um item da lista
lista1[0] = "z"
print(lista1)