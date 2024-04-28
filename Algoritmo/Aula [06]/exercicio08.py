print("==============================")
total = float(input("Informe o total: "))
itens = int(input("Informe a quantidade de itens: "))

if itens > 10 and total > 100:
    desconto = total * 0.15
else:
    desconto = total * 0.06

print("Terá desconto de R$" + str(round(desconto)))
print("==============================")