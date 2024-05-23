soma = 0
quantidade = int(input("Informe a quantidade de pessoas: "))

for i in range(quantidade):
    idade = int(input("Informe sua idade: "))
    soma += idade

print("O valor da soma é:",soma)