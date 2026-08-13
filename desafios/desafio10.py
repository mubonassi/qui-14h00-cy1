print("| Calculo de Compras |")

produto1 = float(input("Digite o valor do 1º produto: "))
produto2 = float(input("Digite o valor do 2º produto: "))
produto3 = float(input("Digite o valor do 3º produto: "))

total = produto1+produto2+produto3

credito = total * 1.078
debito = total
vista = total * 0.95

print("-"*30)
print("> Formas de Pagamento <")
print(f"Crédito: R${credito}")
print(f"Débito: R${debito}")
print(f"À Vista: R${vista}")