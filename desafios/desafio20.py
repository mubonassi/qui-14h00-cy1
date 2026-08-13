print("| CALCULADORA COMPLETA (V2) |")
print("-"*30)
print("> Digite os números a serem operados:")
numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))

print("> Escolha um dos operadores: + - / * **")
op = input("Operador: ")

if op == "+":
    resultado = numero1+numero2
elif op == "-":
    resultado = numero1-numero2
elif op == "/":
    if numero2 != 0:
        resultado = numero1/numero2
    else:
        print("PO! NÃO SE PODE DIVIDIR POR ZERO!!!!!111")
        resultado = False
elif op == "*":
    resultado = numero1*numero2
elif op == "**":
    resultado = numero1**numero2
else:
    print("ERRO! Você não escolheu um operador correto!")
    resultado = False

if resultado != False:
    print(f"{numero1} {op} {numero2} = {resultado}")