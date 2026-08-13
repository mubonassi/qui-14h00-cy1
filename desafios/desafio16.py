print("| ENTREVISTA DE'MPREGO! |")

nome = input("Digite aqui o seu nome: ")
print("* responda com 'sim' ou 'não' *")
resposta = input(f"Você veio para a entrevista, {nome}?: ")

if resposta == "sim":
    print("Beleza, continuando, então!")
    resposta = input(f"Você trouxe o currículo, {nome}?: ")
    if resposta == "sim":
        print("Legal, legal, agora vai dar bom!")
        resposta = input(f"Você tem experiência na área?: ")
        if resposta == "sim":
            print(f"Legal, {nome}! Tudo certo para nossa entrevista!")
        else:
            print("Po, tropeçou na linha de chegada, precisa de experiência na área")
    else:
        print(f"Desculpa, {nome}, mas preciso do seu currículo, vai lá pegar, agora!")
else:
    print("Ué, por que você veio, então?")