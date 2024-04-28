print("==============================")
aluguel = float(input("Informe o valor do aluguel: "))
area = float(input("Informe a área do terreno em metros: "))
total = float(input("Informe o valor do total: "))

if area > 50:
    if total > 350000:
        if aluguel > 1800:
            preco = aluguel * 12 + total
        else:
            preco = aluguel * 6 + total
    else:
        preco = aluguel + total
else:
    preco = total * 1.12

print("O preço de venda será de R$" + str(round(preco, 2)))
print("==============================")