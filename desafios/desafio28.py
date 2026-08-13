print("| PARES E IMPARES |")
print("-"*40)

intervalo = int(input("Digite o intervalo de números à ser mostrado: "))

#Solução 1 - Criando a Lista
pares = []
for i in range(2,intervalo+1,2):
    pares.append(i)
print(f"Pares: {pares}")

#Solução 2 - Usando puramente string
impares = ""
for i in range(1,intervalo+1,2):
    #impares = impares + str(i) + " "
    impares += str(i) + " "
print(f"Impares: {impares}")