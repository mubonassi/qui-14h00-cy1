print("| Z-TYPE GENÉRICO! (treinamento de digitação) |")
print("-"*40)

lista = ["Paralelepípedo","Fusão","Ovo","que"]
acertos = 0
erros = 0

print("Digite as palavras corretamente abaixo!")
for palavra in lista:
    print(f"Palavra: '{palavra}'")
    tentativa = input("Digite aqui: ")
    if tentativa == palavra:
        print("Acertou!")
        acertos += 1
    else:
        print("Errou!")
        erros += 1

if erros == 0:
    print("Parabéns! Você ACERTOU TODOS! WUUUUHAAAAAAA!")
elif acertos == 0:
    print("...pera, acertou nenhum?")
else:
    print(f"Você concluiu! Você acertou {acertos} palavras! E errou {erros} palavras!")