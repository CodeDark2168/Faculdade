n = int(input("Informe a quantidade de vendas: "))
soma = 0

while n > 0:
    venda = float(input("Informe o total da venda: "))
    soma += venda
    n -= 1
    
if soma > 500:
    imposto = soma * 0.15
else:
    imposto = soma * 0.11

print("O imposto será de:",imposto)