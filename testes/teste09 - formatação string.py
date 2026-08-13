#Formatação e Manipulção de Strings/Print

palavra = "garraFA"
frase = "Isso aqui é definitivamente uma frase aleatória"

#Formatação de String - Usando funções existentes na string

#função upper() -> deixa tudo maiusculo
print(palavra.upper())

#função lower() -> deixa tudo minusculo
print(palavra.lower())

#função capitalize() -> deixa o primeiro caractere da string maiuscula
print(palavra.capitalize())

#função title() -> deixa o primeiro caractere de cada palavra da string maiuscula
print(frase.title())

#também é possível usar essas funções em um input()
#palavra = input().lower()

#Funções no print (Devem ser executadas ao lado do F String)
numero1 = 1
numero2 = 3
resultado = 1/3
print(f"{numero1}/{numero2} = {resultado} << Sem formatação")

#função :.Xf
#Limitando casas decimais do float no print
print(f"{numero1}/{numero2} = {resultado:.2f} << Com formatação")