soma = 0
quantidade = int(input("Informe a quantidade de notas: "))

for i in range(quantidade):
    nota = int(input("Informe a nota: "))
    soma += nota

media = soma / quantidade

if media > 7:
    print("Aprovado")
else: 
    print("Reprovado")