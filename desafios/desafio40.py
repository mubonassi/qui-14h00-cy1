def rankear():
    print("| SISTEMA DE RANKING MORKISMOOK |")
    pontos = int(input("Quantos morkis você mookou?: "))

    if pontos >= 1000:
        rank = "Lendário"
    elif pontos >= 700:
        rank = "Mestre"
    elif pontos >= 500:
        rank = "Campeão"
    elif pontos >= 200:
        rank = "Veterano"
    elif pontos > 0:
        rank = "Iniciante"
    else:
        rank = "Mds, que noob"

    return rank

print("| ADAPTANDO FUNÇÃO COM RETURN |")
print("-"*40)

rankeado = rankear()
print(f"Seu rank é: {rankeado}")