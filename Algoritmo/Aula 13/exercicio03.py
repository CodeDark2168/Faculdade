n = int(input("Informe o valor de n: "))
array = []
count1 = 0
count2 = 0
count3 = 0

for i in range(n):
    valor = int(input("Informe um valor: "))
    array.append(valor)

for i in array:
    if i == 0:
        count1 += 1
    elif i >= 0:
        count2 += 1
    else:
        count3 += 1

print(count1,"valores iguais que 0")
print(count2,"valores maiores que 0")
print(count3,"valores menores que 0")