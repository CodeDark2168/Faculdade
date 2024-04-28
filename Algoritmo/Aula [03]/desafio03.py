print("==============================")
real = float(input("Digite o valor em reais: "))
dolar = real / 4.93
euro = real / 5.4
peso = real / 0.0058
iene = real / 0.033
print("==============================")
print("O valor na cotação atual da data que esse programa foi feito é: ")
print(str(round(dolar, 2)) + " dolares")
print(str(round(euro, 2)) + " euros")
print(str(round(peso, 2)) + " pesos angentinos")
print(str(round(iene, 2)) + " ienes")
print("==============================")
