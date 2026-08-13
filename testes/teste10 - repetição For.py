#Estruturas de Repetição
#São estruturas/controle de código que permite que um bloco de comandos possa ser repetido por um número de vezes

#FOR - Repetição contada (quantidade definida) - É determinado quantas X o código será executado

#range(x) - que define quantas vezes/intervalo o código será executado
#i - variável que irá guardar o indice da contagem

#[0,1,2,3]
for i in range(5): #esse código será executado 5x
    print("teste")
print("Fim da repetição")

#Utilizando a variavel da repetição no contexo do código
for i in range(5):
    print(f"Repetição #{i}")
print("Fim da repetição")

#Determinando em qual indice(numero) irá começar a repetição no range(x)
#[1,2,3,4,5]
for i in range(1,5+1):
    print(f"Repetição #{i}")
print("Fim da repetição")

#Determinando os intervalos do range(x)
#[10,20,30,40,50,60,70,80,90,100]
for i in range(10,101,10):
    print(f"Repetição #{i}")

lista = ["a","b","c","d","e","f","g"]
#["a","b"...]
for i in lista:
    print(i)
print("Fim da repetição")

#["b","a","t","a","t","a"]
for i in "batata":
    print(i)
print("Fim da repetição")