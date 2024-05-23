cidades = []

for i in range(5):
    cidade = input(f"Digite o nome da cidade {i+1}: ")
    cidades.append(cidade)

cidades.sort()

print("Cidades em ordem alfabética:")
for cidade in cidades:
    print(cidade)

# O programa cria uma array de cidade vazio, depois executará o for
# pedindo para o usuário digitar o nome que será adiocionada a
# array. Depois ele usara as funções sort para reordenar em ordem alfabetica.

cidades = []

for i in range(5):
    nome = input("Informe o nome da cidade: ")
    populacao = int(input("Informe o número de população: "))
    cidade = [nome,populacao]
    cidades.append(cidade)

cidades.sort()

print("Cidades em ordem alfabética:")
for cidade in cidades:
    print(cidade[0],cidade[1])
