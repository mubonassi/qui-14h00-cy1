import random

print("| LANÇADOR DE DADOS |")

lados = int(input(">> Digite a quantidade de lados do seu [dado]: "))

while True:
    dado = random.randint(1,lados)
    print(f"Dado [D{lados}]: {dado}")

    print("Aperte enter para gerar um novo ou digite 'sair'...")
    escolha = input("")

    if escolha == "sair":
        break