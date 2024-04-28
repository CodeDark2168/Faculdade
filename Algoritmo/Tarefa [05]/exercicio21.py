print("==============================")
codigo = input("Informe o código do produto: ")
quantidade = int(input("Informe a qunatidade: "))
if codigo == "ABCD":
    valor = 5.30
elif codigo == "XYPK":
    valor = 6.00
elif codigo == "KLMP":
    valor = 3.20
elif codigo == "QRST":
    valor = 2.50
else:
    valor = 0
    
if valor > 0:
    total = valor * quantidade
    print("O total a pagar é de R$" + str(total))
else:
    print("Código Inválido")
print("==============================")