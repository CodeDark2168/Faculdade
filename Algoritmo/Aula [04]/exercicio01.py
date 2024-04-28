import math

print("==============================")
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
valorC = int(input("Digite o valor de C: "))
calculo = math.sqrt((valorA**2) + (valorB**2) + (valorC**2))
print("O resultado do calculo √A² + B² + C² é " + str(round(calculo, 2)))
print("==============================")
