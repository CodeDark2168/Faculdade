import math

print("==============================")
largura = float(input("Digite o valor da largura: "))
comprimento = float(input("Digite o valor do comprimento: "))
calculo = math.sqrt(math.pow(largura, 2) + math.pow(comprimento, 2))
print("O resultado da diagonal é " + str(round(calculo, 2)))
print("==============================")
