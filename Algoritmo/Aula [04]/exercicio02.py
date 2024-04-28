import math

print("==============================")
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
calculo = math.sqrt(math.sin(valorA) + math.sin(valorB))
print("O resultado do calculo √senA + senB é " + str(round(calculo, 2)))
print("==============================")
