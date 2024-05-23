n = int(input("Informe a quantidade de notas: "))
count = n
soma = 0

while count > 0:
    nota = int(input("Informe a nota: "))
    count -= 1
    soma += nota

media = soma / n

if media > 7:
    print("Aprovado")
else: 
    print("Reprovado")