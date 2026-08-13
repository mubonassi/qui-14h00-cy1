#Verificando Lista

#Utilizando o comparador IN -> Verificar dentro do valor
lista = ["a","b","c","d"]
item = input("Digite o valor de um item: ")

if item in lista:
    print("Você escreveu um item da lista!")
else:
    print("Poxa, não escreveu um item da lista")

#Utilizando o comparador NOT IN -> Verificar se não está dentro do valor

item = input("Digite um valor QUE NÃO EXISTE: ")

if item not in lista:
    print("Irru, não tem na lista")
else:
    print("Poxa, acertou um da lista")

#Utilizando o NOT com outros comparadores além do IN
if not 1 > 2:
    print("1 menor que 2")