#Break e Quit()

#Break é uma palavra chave que funciona apenas em fluxo de repetição
#O break encerra o fluxo de repetição
for i in range(100000000000000000000000000):
    print(i)
    if i >= 5:
        break
print("Fim da repetição")

#Função quit() encerra o algoritmo
for i in range(10000000000000000000000000):
    print(i)
    if i >= 5:
        quit()
print("VOCÊ NÃO VERÁ ESSE PRINT!")