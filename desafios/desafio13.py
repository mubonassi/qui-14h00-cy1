print("| VERIFICADOR DE POSITIVO OU NEGATIVO |")

numero = int(input("Digite um número para ser verificado: "))

if numero > 0:
    print(f"O número {numero} é positivo!")
else:
    if numero == 0:
        print(f"O número {numero} é neutro!")
    else:
        print(f"O número {numero} é negativo!")