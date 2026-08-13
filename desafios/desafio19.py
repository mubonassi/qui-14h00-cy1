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