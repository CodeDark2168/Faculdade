import math

print("==============================")
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
valorC = int(input("Digite o valor de C: "))
calculo = math.sqrt(valorA) + math.sqrt(valorB) + math.sqrt(valorC)
print("O resultado do calculo √A + √B + √C é " + str(round(calculo, 2)))
print("==============================")
