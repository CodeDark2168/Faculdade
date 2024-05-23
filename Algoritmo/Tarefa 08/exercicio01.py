idades = []

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

idade_mais_alta = max(idades)
idade_mais_baixa = min(idades)

print(f"A idade mais alta é: {idade_mais_alta}")
print(f"A idade mais baixa é: {idade_mais_baixa}")

# O programa cria uma array de idade vazio, depois executará o for
# pedindo para o usuário digitar uma idade que será adiocionada a
# array. Depois ele usara as funções max e min para achar o maioe
# e o menor valor de cada, pára no final mostrar na tela.

notas = []

for i in range(5):
    nome = input("Informe o nome do aluno: ")
    nota = float(input("Informe a nota do aluno: "))
    aluno = [nota,nome]
    notas.append(aluno)

nota_mais_alta = max(notas)
nota_mais_baixa = min(notas)

print("A nota mais alta é",nota_mais_alta[0],"do aluno",nota_mais_alta[1])
print("A nota mais baixa é",nota_mais_baixa[0],"do aluno",nota_mais_baixa[1])