def convMb(mega):
    conv = mega / 1024
    return conv

def convKm(km):
    conv = km * 1000
    return conv

def convMl(ml):
    conv = ml * 1000
    return conv

def convC(c):
    conv = (c*1.8)+32
    return conv

def convDol(dol):
    conv = dol * 5.1729
    return conv

def convTon(ton):
    conv = ton * 1000
    return conv

print("| CAIXA DE FERRAMENTAS DE CONVERSÃO |")

while True:
    print("-"*60)
    print("| ESCOLHA UMA DAS FERRAMENTAS ABAIXO |")
    print("> 1) Mega > Giga")
    print("> 2) Km > M")
    print("> 3) Ml > Lt")
    print("> 4) ºC > ºF")
    print("> 5) US$ > R$")
    print("> 6) Ton > KG")
    print("> 0) Sair")
    print("-"*60)
    escolha = input("-- Digite aqui a opção: ")

    if escolha in ["1","2","3","4","5","6"]:
        valor = float(input(">> Digite aqui o valor para ser convertido: "))
        if escolha == "1":
            convertido = convMb(valor)
            conversao = "GB"
        elif escolha == "2":
            convertido = convKm(valor)
            conversao = "M"
        elif escolha == "3":
            convertido = convMl(valor)
            conversao = "Lt"
        elif escolha == "4":
            convertido = convC(valor)
            conversao = "ºF"
        elif escolha == "5":
            convertido = convDol(valor)
            conversao = "R$"
        elif escolha == "6":
            convertido = convTon(valor)
            conversao = "KG"
        elif escolha == "0":
            break
        print(f"Valor convertido: {convertido}{conversao}")
    else:
        print("**POR FAVOR, ESCOLHA UMA OPÇÃO CERTA, SEU COISÃO**")