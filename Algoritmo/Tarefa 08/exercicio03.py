alturas = []

for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    alturas.append(altura)

contador = 0
for altura in alturas:
    if altura > 1.80:
        contador += 1

print(f"{contador} pessoas têm altura superior a 1.80 metro.")

# O programa cria uma array de alturas vazio, depois executará o for
# pedindo para o usuário digitar a altura que será adiocionada a
# array. Depois usando o for fará um contador para ver qunatas pessoas
# tem mais de 1.80 de altura.

alturas = []

for i in range(5):
    altura = float(input("Informe a altura da pessoa (em metros): "))
    alturas.append(altura)

contador1 = 0
contador2 = 0
for altura in alturas:
    if altura > 1.80:
        contador1 += 1
    elif altura > 1.50:
        contador2 += 1

print(contador1,"pessoas têm altura superior a 1.80 metro.")
print(contador2,"pessoas têm altura superior a 1.50 metro.")

