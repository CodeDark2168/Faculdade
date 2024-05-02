maior = 0

for i in range(10):
    valor = int(input("Informe um valor: "))
    if valor > maior:
        maior = valor

print(maior,"é o maior número.")