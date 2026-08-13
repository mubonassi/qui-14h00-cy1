#Estrutura de Repetição - Repetição Condicionada - WHILE
#While -> Repete enquanto a condição for verdadeira
#Se (condição) então (repete)

numero = 0
while numero == 0:
    numero = int(input("Digite um número diferente de zero: "))
    if numero == 0:
        print("MAS TEM QUE SER DIFERENTE!!!!!")

#Repetição Indefinida -> Loop infinito

while True:
    escolha = input("Digite 'sair' para encerrar o código: ")
    if escolha == "sair":
        break