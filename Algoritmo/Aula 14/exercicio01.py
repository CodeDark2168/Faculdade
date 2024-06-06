n = int(input("Informe o valor de N: "))
array = []

for i in range(n):
    valor = int(input(f"Informe o valor {i}: "))
    array.append(valor)

for i in range(len(array)):
    if i % 2 == 0:
        print(f"Posição {i}, número {array[i]}")