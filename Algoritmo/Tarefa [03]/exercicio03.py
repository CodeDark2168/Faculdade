import math

print("==============================")
valorAtual = int(input("Digite o valor atual: "))
taxaJuros = int(input("Digite o valor da taxa de juros: "))
anos = int(input("Digite a quantidade de anos: "))
calculo = valorAtual * math.pow(1 + (taxaJuros/100), anos)
print("O valor futuro será de " + str(round(calculo, 2)))
print("==============================")
