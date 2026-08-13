print("| SOMANDO COM OS INTERVALOS |")
print("-"*40)

intervalo = int(input("Digite a quantidade de números que deseja somar: "))
resultado = 0
conta = ""

for i in range(1,intervalo+1):
    numero = float(input(f"Digite o número {i}: "))
    if numero < 0:
        print("Não se pode negativo! O valor somado será zero!")
        numero = 0.0

    resultado += numero
    conta += str(numero)

    if i < intervalo:
        conta += " + "

print(f"{conta} = {resultado}")