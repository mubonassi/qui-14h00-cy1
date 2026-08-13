print("| ABASTECENDO UM CARRO |")
print("-"*30)

limite = float(input("Digite o quanto de limite (L) o seu tanque possui: "))
falta = float(input("Digite o quanto está faltando (L) no seu tanque: "))

if falta > limite:
    print("ERRO: Falta está acima do limite!")
else:
    abastece = float(input("Digite o quanto você deseja abastecer (L): "))
    if abastece > falta:
        print("ERRO: Valor abastecido maior que o limite!")
    else:
        tanque = limite - falta + abastece
        print(f"ABASTECIDO COM SUCESSO!\nTotal no tanque: {tanque}")