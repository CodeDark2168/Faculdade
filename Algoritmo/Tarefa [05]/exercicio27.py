IPI = float(input('Digite a porcentagem do IPI (Ex: 5 para 5%): '))

código1 = int(input('Digite o código da peça 1: '))
valor1 = float(input('Digite o valor da peça 1: '))
quantidade1 = int(input('Digite a quantidade da peça 1: '))

código2 = int(input('Digite o código da peça 2: '))
valor2 = float(input('Digite o valor da peça 2: '))
quantidade2 = int(input('Digite a quantidade da peça 2: '))

total = (valor1 * quantidade1 + valor2 * quantidade2) * (IPI/100 + 1)

print('O total a ser pago é de R$' + str(round(total,2)))