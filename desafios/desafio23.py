print("| GERENCIANDO TURMA |")

#Pt.1 - Cadastrando alunos
listaAlunos = ['Murilo','Pedro','Pietro','Heitor']
print(f"Lista de alunos: {listaAlunos}")
print("-"*30)
print("Cadastre 3 alunos abaixo!")
aluno1 = input("Digite aqui o nome do #1 aluno: ")
aluno2 = input("Digite aqui o nome do #2 aluno: ")
aluno3 = input("Digite aqui o nome do #3 aluno: ")
listaAlunos.extend([aluno1,aluno2,aluno3])

#Escolher umas das oções (remover, atualizar ou adicionar)
print("Escolha quais das operações você deseja realizar na lista")
print("1) Remover 2) Atualizar Nome 3) Adicionar 1 aluno")
escolha = input("Digite aqui a opção: ")

if escolha == "1":
    aluno = input("Digite o nome do aluno que deseja remover: ")
    listaAlunos.remove(aluno)
elif escolha == "2":
    aluno = int(input("Digite o indice do aluno que deseja mudar o nome: "))
    nome = input("Digite o novo nome: ")
    listaAlunos[aluno] = nome
elif escolha == "3":
    aluno = input("Digite o nome do aluno que deseja adicionar: ")
    listaAlunos.append(aluno)
else:
    print("oi?")

print(f"Lista Final: {listaAlunos}")