print("| CONVIDADOS E BANIDOS |")
print("-"*30)

funcionarios = ["Murilo","3.14tro","Peter","Hey-Thor","Funcionário Ctrl+Play","Pietro","Pedro","Heitor","Mauricia","Mauricio de Souza","Cosplay de T-Rex","Felipe","Vitor","Fernando","Miniatura de t-Rexxy"]
banidos = ["Murilo","Peter","3.14tro","Hey-Thor","Cosplay de T-Rex"]

print("Faça a verificação de convite da festa da empresa!")
print("Mas, primeiro, deseja banir algum funcionário? (S/N)")
resposta = input("Digite aqui: ")

if resposta.upper() == "S":
    print("Então, escolha um funcionário para ser banido!")
    resposta = input("Digite aqui: ")
    if resposta in funcionarios and resposta not in banidos:
        banidos.append(resposta)
    else:
        print("Funcionário inválido! Verifique se existe ou já está banido")

print("Continuando! Agora digite o convidado que está entrando na festa!")
resposta = input("Digite aqui: ")

if resposta in funcionarios:
    print("O funcionário existe!")
    if resposta not in banidos:
        print("E poderá entrar!")
    else:
        print("Mas está banido!")
else:
    print("O funcionário não existe!")