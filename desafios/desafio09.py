print("| AUMENTO NA CONTA BANCARIA |")

contaBancaria = float(input("> Digite o valor da sua conta bancária (R$): "))
aumento = int(input("> Digite a % de aumento da sua conta: %"))

contaBancaria = contaBancaria * (aumento/100 + 1)

print(f"Valor Final da Conta Bancária: R${contaBancaria}")