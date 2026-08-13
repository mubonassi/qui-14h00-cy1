#Estruturas de Condição -> Criam condições para que um bloco de código seja executado
#Um comando só irá acontecer se determinada condição retornar verdadeira
#Condição > Ação
#Ex: Se o número digitado for 48 acontecerá a mensagem "você digitou o número 48"

numero = int(input("Digite um número para ser verificado: "))

#se (condição) então {ação}
if numero == 48:
    print("Você digitou o número 48")
#senão {ação}
else:
    print("Você NÃO digitou o número 48")

#Comparadores
# == -> Igual a (valor == valor)
# > -> Maior que (valor > valor)
# < -> Menor que (valor < valor)
# >= -> Maior ou igual a (valor >= valor)
# <= -> Menor ou igual a (valor <= valor)
# != -> Diferente de (valor != valor)

#Diferença entre = e ==
# = -> Atribuição -> Nome = "Pietro" -> O nome é Pietro
# == -> Comparação -> Nome == "Heitor" -> O nome é Heitor?