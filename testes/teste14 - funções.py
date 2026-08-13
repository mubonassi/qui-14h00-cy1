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

print()