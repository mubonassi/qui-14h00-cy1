print("| VERSÃO FINAL DE CALCULO DE MÉDIA |")

nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
nota3 = float(input("Digite a Nota 3: "))

media = (nota1+nota2+nota3)/3

mediaMinima = float(input("Digite a média mínima da sua escola: "))

print(f"Média final: {media}")
if media >= mediaMinima:
    print("Situação: aprovado")
else:
    print("Situação: reprovado")