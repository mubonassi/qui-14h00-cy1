valor = 0

def funcao1():
    global valor
    valor += 10

def funcao2():
    global valor
    valor -= 10

print(valor)