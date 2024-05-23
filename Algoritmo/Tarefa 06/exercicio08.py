pares = 0

for i in range(10):
    valor = int(input("Informe um valor: "))
    if valor % 2 == 0:
        pares += 1

print(pares,"números são números pares.")