print("| SORVETERIA COMPLETA |")
print("-"*30)

sorvetes = ["Chocolate","Morango","Baunilha","Flocos","Abacaxi com Vinho","T-Rex","Manga","Chá"]
coberturas = ["Chocolate","Chocolate Branco","MM's","Nutella","Ninho","t-Rexxy","Fini"]

print("Selecione um dos sorvetes abaixo!")
print(f"Cardapio: {sorvetes}")
sorvete = input("Digite aqui a sua escolha: ")

if sorvete in sorvetes:
    print("Selecione uma das coberturas abaixo!")
    print(f"Cardapio: {coberturas}")
    cobertura = input("Digite aqui sua escolha: ")
    if cobertura in coberturas:
        print(f"Está aqui! O seu sorvete de {sorvete} com {cobertura}! Um mião de reais, me dá!")
    else:
        print(f"Sinto muito, a cobertura {cobertura} não está no nosso cardápio, ficará só o sorvete {sorvete} sem nada mesmo")
else:
    print(f"Sinto muito, o sorvete {sorvete} não está no nosso cardápio. Nem sei se {sorvete} existe. O que diabos é {sorvete}?")