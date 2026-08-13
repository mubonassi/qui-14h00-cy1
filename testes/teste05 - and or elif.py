#Estrutura de condição ENCADEADA e COMPOSTA
numero = int(input("Digite um número: "))

#IF Composto (AND e OR) -> Trabalhando com múltiplas condições
#AND (e) -> Todas as condições necessitam ser verdadeiras
if numero >= 0 and numero <= 10:
    print("Você digitou um número entre 0 a 10")
else:
    print("Você NÃO digitou um número entre 0 a 10")

#OR (ou) -> Uma das condições necessitam ser verdadeiras
if numero == 6 or numero == 9:
    print("Você encontrou um número mágico!")
else:
    print("Você não encontrou um número mágico!")

#IF Encadeado -> Trabalhando com múltiplas perguntas/estruturas
#elif -> Uma condição caso a anterior tenha sido negativa
if numero > 0:
    print("O número é positivo!")
elif numero < 0:
    print("O número é negativo!")
else:
    print("O número é neutro!")