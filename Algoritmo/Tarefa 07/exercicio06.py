n = int(input("Informe a quantidade de compras: "))
soma_cartao = 0
soma_dinheiro = 0

while n > 0:
    valor = float(input("Informe o valor da compra: "))
    pagamento = input("Informe a forma de pagamento: ")
    n -= 1

    if pagamento == "Dinheiro":
        soma_dinheiro += valor
    else:
        soma_cartao += valor

print("Será cobrado R$",soma_dinheiro,"no dinheiro e R$",soma_cartao,"no cartão.")
