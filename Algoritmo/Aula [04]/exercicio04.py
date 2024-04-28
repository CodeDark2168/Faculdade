import math

print("==============================")
populacaoAtual = int(input("Digite o valor da população atual: "))
taxaCrescimento = int(input("Digite o valor da taxa de crescimento: "))
anos = int(input("Digite o valor de anos: "))
calculo = populacaoAtual * math.pow(1 + (taxaCrescimento/100), anos)
print("A população futura será equilatente a " + str(round(calculo, 2)))
print("==============================")
