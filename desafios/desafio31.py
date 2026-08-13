print("| RESTAURANTE PYTHON |")
print("-"*40)

cardapio = ["Hamburger","X-Burger","Burger-X","T-Rex","Salada","Xbox","Playstation","Salada 2"]

print("--- Cardapio ---")
for prato in cardapio:
    print(f">> {prato}")

escolha = input("Digite qual prato deseja pedir: ")

if escolha in cardapio:
    print(f"Você escolheu o prato {escolha}!")
else:
    print(f"Desculpa, o prato {escolha} está indisponível")