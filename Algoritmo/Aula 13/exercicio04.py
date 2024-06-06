vetorA = []
vetorB = []
vetorC = []

for i in range(4):
    valor = int(input("Informe um valor: "))
    vetorA.append(valor)

for i in range(4):
    valor = int(input("Informe um valor: "))
    vetorB.append(valor)

for i in range(4):
    resultado = vetorA[i] + vetorB[i]
    vetorC.append(resultado)

print(vetorC)