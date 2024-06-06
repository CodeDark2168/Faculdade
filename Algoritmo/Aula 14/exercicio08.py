n = int(input("Informe o valor de N: "))
array = [0] * n
produto = 1

for i in range(n):
    valor = int(input(f"Informe o valor {i}: "))
    array[i] = valor

for i in range(len(array)):
    if i % 2 != 0:
        produto *= array[i]

print(f"O produto dos numéros será de {produto}")