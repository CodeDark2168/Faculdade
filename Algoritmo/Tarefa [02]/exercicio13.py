print("==============================")
valorPrincipal = float(input("Digite o valor principal: "))
taxaJuros = float(input("Digite a taxa de juros anual (ex: 5 para 5%): "))
periodoAnos = int(input("Digite o período em anos: "))
jurosSimples = valorPrincipal * (taxaJuros / 100) * periodoAnos
valorFinal = valorPrincipal + jurosSimples
print("==============================")
print("O valor dos juros simples é: R$" + str(jurosSimples))
print("O valor final a ser pago é: R$" + str(valorFinal))
print("==============================")
