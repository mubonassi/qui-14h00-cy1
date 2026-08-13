#Manipulando lista em Python

lista = []

#Funções de manipulação da lista

# -- Adicionando itens na lista
#Append -> Adiciona um item no final da lista
item = input("Digite um item para adicionar na lista: ")
lista.append(item)
print(lista)

item = input("Digite OUTRO item para adicionar na lista: ")
lista.append(item)
print(lista)

lista.append(input("Digite MAIS UM item para adicionar na lista: "))
print(lista)

#Extend -> Adiciona multiplos itens na lista
item1 = input("Digite o #1 item: ")
item2 = input("Digite o #2 item: ")
item3 = input("Digite o #3 item: ")

lista.extend([item1,item2,item3])
print(lista)

#-- Remover itens da lista
#Remove -> Remove o item pelo VALOR
tirar = input("Digite o valor do item que deseja deletar: ")
lista.remove(tirar)
print(lista)

#Pop -> Remove o item pelo INDEX (indice)
tirar = int(input("Digite a indice do item que deseja deletar: "))
lista.pop(tirar)
print(lista)