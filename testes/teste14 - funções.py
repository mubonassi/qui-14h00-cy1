#Funções

#Funções do Sistema: Bloco de Comandos pré-prontos pela linguagem que te permite executar instruções
#Funções do Código/Scrip: Bloco de Comandos criados dentro do script

#Como criar uma função
#Usando o 'def' -> definição

#Função Simples: Simplesmente executa os comandos dados
def faleHelloWorld():
    print("Hello, World!")
    print("Pronto!")

faleHelloWorld()

#Função com Return
#Variaveis dentro de uma função não são globais
#Variavel global -> Pode ser acessado por todos dentro do script
#Uma variavel criada na função pertence apenas a função

#Return -> Exporta um valor/variavel para fora da função
def somarNumeros():
    soma = 10+20
    return soma

valor = somarNumeros()
print(valor)
print("-"*40)
#Função com parametro
#Parametros: são variaveis iniciais da função que necessitam ser preenchidas externamente por quem chamou a função
def calcularNumeros(n1,n2):
    calculo = n1**n2
    print(calculo)

calcularNumeros(10,20)
calcularNumeros(3,5)
calcularNumeros(2,9)

def realizarConta(n1,n2):
    conta = n1/n2*n1+n2**n1+n2//n1
    return conta

print("-"*40)
conta1 = realizarConta(10,30)
conta2 = realizarConta(5,3)
conta3 = realizarConta(8,2)
print(conta1)
print(conta2)
print(conta3)