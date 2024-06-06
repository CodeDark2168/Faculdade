n = int(input("Informe o valor de N: "))
array = [0] * n
soma = 0

for i in range(n):
    valor = float(input(f"Informe o valor {i}: "))
    array[i] = valor

for i in range(len(array)):
    if i % 2 == 0:
        soma += array[i]

print(f"O valor da soma será de {soma}") 