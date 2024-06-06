n = int(input("Informe o valor de N: "))
array = [0] * n

for i in range(len(array)):
    nome = input("Informe um nome: ")
    array[i] = nome

print("\nPosições pares:")

for i in range(len(array)):
    if i % 2 == 0:
        print(f"Posição {i}, {array[i]}")

print("\nPosições ímpares:")

for i in range(len(array)):
    if i % 2 != 0:
        print(f"Posição {i}, {array[i]}")