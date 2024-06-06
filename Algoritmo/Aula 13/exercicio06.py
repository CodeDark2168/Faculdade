n = int(input("Informe o valor de n: "))
valores = []
pares = []
impares = []

for i in range(n):
    valor = int(input("Informe um valor: "))
    valores.append(valor)

for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Valores:",valores)
print("Pares:",pares)
print("Ímpares:",impares)