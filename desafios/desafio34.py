print("| Autenticação de Ferramenta |")
print("-"*60)

usuarios = ["Murilo","Peter","3.14etro","Hey! Thor!","T-Rex Admin"]

for i in range(3):
    usuario = input("Digite aqui o nome do usuário: ")
    if usuario in usuarios:
        print("Usuário autenticado!")
        print("Iniciando sistema...")
        break
    else:
        print("Usuário inexistente!")
        if i >= 2:
            print("CONTA BLOQUEADA!")
            quit()

print("| COMPRANDO PRODUTO |")
print("-"*30)

listaProdutos = ["Xbox","Playstation","Nintendo","Polystation","Beyblade","Atari","Nerf","Salada de T-Rex"]

print(f"Lista de Produtos: {listaProdutos}")

print("Selecione um Produto!")
produto = int(input("Digite aqui: "))
print(f"Produto selecionado: {listaProdutos[produto]}")

listaProdutos[produto] = "Comprado"
print(f"Lista de Produtos: {listaProdutos}")