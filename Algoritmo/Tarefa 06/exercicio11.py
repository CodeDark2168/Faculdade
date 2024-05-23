valor = int(input("Informe um valor: "))
menor = valor
maior = 0

for i in range(9):
    valor = int(input("Informe um valor: "))
    if valor < menor:
        menor = valor
    elif valor > maior:
        maior = valor

print(menor,"é o menor número e",maior,"é o maior número.")