print("==============================")
codigo = int(input("Informe o código do produto: "))
quantidade = int(input("Informe a qunatidade: "))
if codigo == 100:
    valor = 1.20
elif codigo == 101:
    valor = 1.30
elif codigo == 102:
    valor = 1.50
elif codigo == 103:
    valor = 1.20
elif codigo == 103:
    valor = 1.20
elif codigo == 104:
    valor = 1.30
elif codigo == 105:
    valor = 1.00
total = valor * quantidade
print("O total a pagar é de R$" + str(total))
print("==============================")