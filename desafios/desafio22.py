print("| COMPRANDO PRODUTO|")
print("-"*30)

listaProdutos = ["Xbox","Playstation","Nintendo","Polystation","Beyblade","Atari","Nerf","Salada de T-Rex"]

print(f"Lista de Produtos: {listaProdutos}")

print("Selecione um Produto!")
produto = int(input("Digite aqui: "))
print(f"Produto selecionado: {listaProdutos[produto]}")

listaProdutos[produto] = "Comprado"
print(f"Lista de Produtos: {listaProdutos}")