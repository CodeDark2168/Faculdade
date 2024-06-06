n = int(input("Informe o valor de N: "))
array = [0] * n
count = 0

for i in range(n):
    valor = int(input(f"Informe o valor {i}: "))
    array[i] = valor

for i in range(len(array)):
    if i % 2 != 0:
        if array[i] % 2 == 0:
            count += 1

print(f"{count} valores são pares em posições ímpares") 