#Guardando/Armazenar Informações
#Variaveis -> Um pedaço na memória do programa para guardar uma informação de qualquer tipo
#Declarando Variaveis -> Nomeia a variável junto de seu valor inicial
#Ex: Variavel = Valor

nome = "Murilo Bonassi" #String
idade = 31 #Int
altura = 1.67 #Float
trabalha = True #Boolean
calculo = 10+20-30*40/50**60 #Lógico -> Guarda o resultado do comando

#Exibindo as Variaveis
#Método 1 - Concatenando Valores
print("Meu nome é",nome)
print("E eu tenho",idade,"anos")

#Método 2 - Formatando String
print(f"Eu tenho {altura}m de altura")
print(f"E minha situação de trabalho é {trabalha}")
print(f"10+20-30*40/50**60 = {calculo}")