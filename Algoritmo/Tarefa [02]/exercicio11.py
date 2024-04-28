print("==============================")
conta = float(input("Digite o valor total da conta: "))
gorjetaPercentual = float(input("Digite a porcentagem de gorjeta desejada (ex: 15 para 15%): "))
gorjetaValor = conta * (gorjetaPercentual / 100)
total = conta + gorjetaValor
print("==============================")
print("O total a ser pago, incluindo a gorjeta de " + str(gorjetaPercentual) + "%, é: " + str(total))
print("==============================")
