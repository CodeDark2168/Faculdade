print("==============================")
precoOriginal = float(input("Digite o preço original do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))
descontoValor = precoOriginal * (desconto / 100)
precoFinal = precoOriginal - descontoValor
print("==============================")
print("O preço final do produto com " + str(desconto) + "% de desconto é: " + str(precoFinal))
print("==============================")
