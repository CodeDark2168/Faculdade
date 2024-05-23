### Exercício 1

- Faça o seguinte programa rodar, explique e tire print do código e da execução.

````
vetor = [10, 20, 30, 40, 50]
for elemento in vetor:
    print(elemento)
````

### Exercício 2

- Teste, explique e tire print de toda a tela.

````
vet_misto = [10, 3.14, "Python", 25, 2.71, "Programação"]
for elemento in vet_misto:
    print(elemento)
````

### Exercício 3

- Rode, teste, explique e tire print panorâmico, faça um for que mostre todos os elementos.

````
meu_vetor = [10, 'Python', -10.55, 0.0001, 50]

elemento_posicao_2 = meu_vetor[2]
print(elemento_posicao_2)

primeiro_elemento = meu_vetor[0]
print(primeiro_elemento)

ultimo_elemento = meu_vetor[-1]
print(ultimo_elemento)  
````

### Exercício 4

- Faça o FOR para mostrar todos os elementos do vetor.

````
vetor = [5.2, 7.8, 3.1, 9.5]
soma = sum(vetor)
print(soma)
````

### Exercício 5

- Aprimore este programa para não permitir o usuário informar um número que extrapole as dimensões do vetor.

````
dias = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado"]
numero = int(input("qual dia quer saber?")

print (dias[numero])
````

### Exercício 06

- Teste e explique.

````
tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho

for i in range(tamanho):
    elemento = input(f"Digite o elemento {i+1}: ")
    vetor[i] = elemento

print("Vetor:", vetor)
````

### Exercício 07

- Altere o programa a seguir para mostrar a média das notas dos alunos.

````
tamanho = int(input("Digite a quantidade de alunos: "))
notas = [0] * tamanho

for i in range(tamanho):
    elemento = input(f"Digite a nota do aluno {i+1}: ")
    notas[i] = elemento

print("Vetor:", notas)
````

### Exercício 08

- Explique o append, o sum e o len.

````
notas = []

for i in range(5):
    nota = float(input(f"Digite a nota da disciplina {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média aritmética das notas é: {media:.2f}")
````