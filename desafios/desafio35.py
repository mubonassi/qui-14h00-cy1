print("| COMPRANDO DO CATÁLOGO |")
print("-"*60)

produtos = ["Xbox","GTA VI - T-Rex Edition","Playstation","Switch","Batata Frita RGB Gamer","Garrafinha sem Buraco","Copo com Dois Buracos"]
valores = [3000,9000,4000,3400,10000,10,20]

for produto in produtos:
    print(f"Produto: {produto}")
    print("Deseja comprar o produto? (S/N)")
    escolha = input("Digite aqui: ").upper()

    if escolha == "S":
        print(f"Você escolheu o produto {produto}")
        indice = produtos.index(produto)
        valor = valores[indice]
        print(f"E o valor dele é R${valor}")
        break

if escolha != "S":
    print("Você não escolheu nenhum dos produtos! Flw!")