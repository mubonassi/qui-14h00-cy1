def cadastrar():
    print("|SISTEMA DE CADASTRO E LOGIN|")
    print("-"*30)
    print("> CADASTRO")
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    print("**Usuário Cadastrado com Sucesso!**")

    print("> LOGIN")
    usuarioLogin = input("Usuário: ")
    senhaLogin = input("Senha: ")

    if usuario == usuarioLogin and senha == senhaLogin:
        print("!!SEJA BEM VINDO!!")
    else:
        print("Erro: Login falhado com sucesso!")

def abastecer():
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

def manipular():
    print("> MANIPULANDO UM NÚMERO")
    numero = float(input("Digite um número: "))

    antecessor = numero - 1
    sucessor = numero + 1
    dobro = numero * 2
    metade = numero / 2

    print(f"O antecessor de {numero} é {antecessor}")
    print(f"O sucessor de {numero} é {sucessor}")
    print(f"O dobro de {numero} é {dobro}")
    print(f"A metade de {numero} é {metade}")

print("| CAIXOSA DE FERRAMENTAS |")
print("-"*40)

while True:
    print(">> Escolha uma das ferramentas (via indice) <<")
    print("1) Cadastrar e Logar")
    print("2) Abastecer o tanque")
    print("3) Manipulando numeros")
    print("4) Sair")
    escolha = input(">> Digite uma das opções: ")

    print("-"*40)
    if escolha == "1":
        cadastrar()
    elif escolha == "2":
        abastecer()
    elif escolha == "3":
        manipular()
    elif escolha == "4":
        break
    else:
        print("que")
    input("Aperte enter para continuar...")
    print("-"*40)