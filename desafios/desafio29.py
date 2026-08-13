print("| SOMANDO OS NÚMEROS NO INTERVALO |")
print("-"*40)

intervalo = int(input("Digite o intervalo dos números que deseja que sejam somados: "))

res = 0
conta = ""
for i in range(1,intervalo+1):
    if i < 0:
        res += 0
    else:
        res += i
    conta += str(i)
    if i < intervalo:
        conta += " + "

print(f"Conta: {conta} = {res}")
