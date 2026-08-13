print("| VERIFICAÇÃO DE CONVITE |")
nome = input("Seu nome aaaaaaaaaaaaaaaaaa: ")
idade = int(input("Fala a sua idade: "))
convite = input("Você tem um convite? (S/N): ")

if idade >= 18 and convite == "S":
    print(f"Seja bem vindo, {nome}! Pode entrar!")
elif idade < 18 and convite == "N":
    print("Tá fazendo o que aqui, então?")
elif idade < 18:
    print(f"Você é novo demais, sai daqui!")
elif convite == "N":
    print(f"Você está bloqueado de entrar nessa festa super maneira, {nome}.")
else:
    print("que?")