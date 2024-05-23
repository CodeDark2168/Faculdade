notas = []

for i in range(5):
    nota = float(input(f"Digite a nota da disciplina {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média aritmética das notas é: {media:.2f}")

# O append irá adicionar o valor ao final da lista, o sum somará os valores da lista e o
# len contará qunatos elemnetos tem na lista.