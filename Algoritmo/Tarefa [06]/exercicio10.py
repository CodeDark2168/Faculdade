valor = int(input("Informe um valor: "))
menor = valor

for i in range(9):
    valor = int(input("Informe um valor: "))
    if valor < menor:
        menor = valor

print(menor,"é o menor número.")