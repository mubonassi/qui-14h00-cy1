import random

print("| SHOW DO PY-LHÃO |")
print("-"*40)

perguntas = ["Qual era a cor do cavalo branco do napoleão?","Quantos anos duraram a guerra dos cem anos?","Quantos meses possuem 28 dias?"]
respostas = ["Preto","116","12"]

indice = random.randint(0,2)
pergunta = perguntas[indice]
resposta = respostas[indice]

erros = 0
tentativa = ""
print("---RESPONDA A PERGUNTA ABAIXO---")

while True:
    print(pergunta)
    tentativa = input("Escreva aqui a resposta (caso queira desistir, escreva 'desisto'): ")
    if tentativa.lower() == resposta.lower():
        print("Yyyyyyaaaaaaaay")
        if erros > 0:
            print(f"Mas você errou {erros} vezes")
        break
    elif tentativa.lower() == "desisto":
        print(f"Desistiu? Então, a resposta era: {resposta}")
        break
    else:
        print("nay")
        erros += 1