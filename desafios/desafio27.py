print("| TABUADA CLÁSSICA |")
print("-"*30)

tabuada = int(input("Digite o número para fazer a tabuada: "))

for i in range(1,11):
    res = tabuada * i
    print(f"{tabuada} x {i} = {res}")