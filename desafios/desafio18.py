print("| SISTEMA DE RANKING MORKISMOOK |")
pontos = int(input("Quantos morkis você mookou?: "))

if pontos >= 1000:
    print("Rank: Lendário")
elif pontos >= 700:
    print("Rank: Mestre")
elif pontos >= 500:
    print("Rank: Campeão")
elif pontos >= 200:
    print("Rank: Veterano")
elif pontos > 0:
    print("Rank: Iniciante")
else:
    print("Mds, que noob")