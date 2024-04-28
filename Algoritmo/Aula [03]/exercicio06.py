print("==============================")
totalCompra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite o valor do desconto: "))
juros = float(input("Digite o valor do juros: "))
totalDescontoJuros = totalCompra - desconto + juros
print("==============================")
print("Sua compra deu R$" + str(totalDescontoJuros))
print("==============================")

