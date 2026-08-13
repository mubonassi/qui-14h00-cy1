print("| CONTADOR DE CARACTERES |")
print("-"*40)

escolha = input("Digite aqui a palavra/frase: ")

contagem = 0
for i in escolha:
    if i != " ":
        contagem += 1

print(f"'{escolha}' tem no total de {contagem} caracteres!")