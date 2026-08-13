print("> AUMENTO DE 10%")

valor = float(input("Digite um valor: "))

#Método 1 - Utilizando uma segunda variável
acrescimo = valor * 1.10 #1
acrescimo = valor + (valor / 10) #2

print(f"O acréscimo de 10% do valor {valor} deu {acrescimo}")

#Método 2 - Alterando a variável
valor = valor * 1.10