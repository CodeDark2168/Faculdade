n = int(input("Informe o valor de N: "))
array = [0] * n
count = 0

for i in range(len(array)):
    nome = input("Informe um nome: ")
    array[i] = nome

l = input("Informe o valor de L: ")

for i in array:
    if i.lower().startswith(l.lower()):
        count += 1

print(f"{count} nomes começam com {l}")
    