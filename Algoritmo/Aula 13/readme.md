## Exercício 01

- Utilize o programa abaixo que lê um vetor de 10 números inteiros e imprima apenas os números ímpares para separadamente mostrar também os PARES.

````
# Criar um vetor para armazenar os números
vetor = []

# Ler os números do usuário
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    vetor.append(num)

# Imprimir os números ímpares
print("Números ímpares:")
for num in vetor:
    if num % 2 != 0:
        print(num)

# agora, imprimir os pares...
````

## Exercício 02

- Explique o programa a seguir, em especial as funções startwith e lower.
Depois, pesquise o endswithe e adicione um novo FOR para mostrar as letras que terminam com A.

````
# Criar um vetor para armazenar as strings
strings = []

# Ler as strings do usuário
for i in range(6):
    string = input(f"Digite a string {i+1}: ")
    strings.append(string)

# Imprimir as strings que começam com 'A'
print("Strings que começam com 'A':")
for string in strings:
    if string.lower().startswith('a'):
        print(string)
````

## Exercício 03

- Faça um programa que pergunte o valor de N para o usuário.
- Em seguida,  leia um vetor de N números inteiros
- Depois, conte quantos números são iguais a zero, quantos números são maiores que zero e quantos números são menores que zero.

## Exercício 04

- Crie um programa que leia dois vetores VETA e VETB de 4 números inteiros cada.
- Depois, calcule a soma dos elementos correspondentes na mesma posição no VETC.
- Por exemplo:
    - VETA= [1,4,6,4]
    - VETB = [6,3,1,0]
    - resultado VETC = [7, 7, 7, 4]

- dica: VETC[i] = VETA[i] + VETB[i]

## Exercício 05

- Faça um Programa que leia um vetor de 10 caracteres (letras)
- Faça um FOR que verifique quantas vogais estão no vetor.
- Imprima essas vogais presentes no vetor.

## Exercício 06

- Faça um Programa que leia N números inteiros (pergunte para o usuário o valor de N) e armazene-os num vetor. 
- Depois, utilize um for para armazene os números pares no vetor VETPAR e os números ímpares no vetor VETIMPAR. 
- Ao final, faça FOR para imprimir cada um dos 3 três vetores.

