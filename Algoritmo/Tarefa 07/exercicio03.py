n = int(input("Informe um valor: "))
soma = 0

while n > 0:
    idade = int(input("Informe sua idade: "))
    n -= 1
    soma += idade

print("O valor da soma é:",soma)