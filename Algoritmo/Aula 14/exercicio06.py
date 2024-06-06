n = int(input("Informe o valor de N: "))
array = [0] * n

for i in range(n):
    valor = int(input(f"Informe o valor {i}: "))
    array[i] = valor

maior = array[0]

for i in range(n):
    if array[i] > maior:
        maior = array[i]

print(f"O maior valor é {maior} posição {i}")