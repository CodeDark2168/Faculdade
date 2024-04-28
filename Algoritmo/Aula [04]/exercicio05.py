import math

print("==============================")
x1 = float(input("Digite o valor de x1: "))
x2 = float(input("Digite o valor de x2: "))
y1 = float(input("Digite o valor de y1: "))
y2 = float(input("Digite o valor de y2: "))
calculo = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
print("O resultado do calculo √(x2-x1)² + (y2-y1)² é " + str(round(calculo, 2)))
print("==============================")
