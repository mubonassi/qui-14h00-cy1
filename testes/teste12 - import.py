#Import - Permite importar funções internas especificas do python


#math - Uma biblioteca de funções matemáticas especificas
import math

#math.floor -> arredonda para baixo
#math.ceil -> arredonda para cima
#math.sqrt -> realiza raiz quadrada
#math.pi -> variavel constante que entrega o pi

num1 = 345
num2 = 37
divisaoBasica = num1/num2
arredondado = math.floor(divisaoBasica)
print(f"Divisão: {divisaoBasica} | Arredondado: {arredondado}")

num = 400
raizQuadrada = math.sqrt(num)
pi = math.pi
print(f"Raiz Quadrada: {raizQuadrada} | Pi: {pi}")

#random - funções que geram valores aleatórios
import random

valor = random.randint(1,100)
print(f"Valor aleatório: {valor}")

lista = ["a","b","c","d","e","f","g"]
item = random.choice(lista)
print(f"Item aleatório: {item}")