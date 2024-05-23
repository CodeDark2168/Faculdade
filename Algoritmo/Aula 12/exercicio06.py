tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho

for i in range(tamanho):
    elemento = input(f"Digite o elemento {i+1}: ")
    vetor[i] = elemento

print("Vetor:", vetor)

# Ele multiplicará o vetor pela variável tamanho para denominar a quantiadde de variáveis que o 
# array guardará, depois com o for o usuário irá inserir cada valor substituindo o zero de cada 
# posição.