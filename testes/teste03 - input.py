#Recebendo Informações
#Função input() -> recebe informações do usuário pelo terminal COMO STRING
#Ex: variavel = input()
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
altura = input("Digite a sua altura: ")
fruta  = input("Digite a sua fruta favorita: ")
jogo = input("Digite o seu jogo favorito: ")

#Exibindo todas as variaveis em um único print
print(f"Seu nome é {nome}, você tem {idade} anos, você mede {altura}m de altura. Sua fruta favorita é {fruta}, e seu jogo favorito é {jogo}")

#Processando/Calculando Informações na Variável
#Operando com Strings
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nomeCompleto = nome + " " + sobrenome
print(f"Seu nome é {nomeCompleto}")

#Operando com Numeros
#Números necessitam de conversão/tradução
#ex: int(valor) / float(valor)
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
resultado = numero1+numero2
print(f"{numero1} + {numero2} = {resultado}")