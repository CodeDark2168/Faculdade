n1 = int(input("Informe a quantidade de provas: "))
n2 = int(input("Informe a quantidade de trabalhos: "))
count1 = n1
count2 = n2
soma_prova = 0
soma_trabalho = 0

while count1 > 0:
    nota = int(input("Informe a nota: "))
    soma_prova += nota
    count1 -= 1

media_prova = soma_prova / n1

while count2 > 0:
    nota = int(input("Informe a nota: "))
    soma_trabalho += nota
    count2 -= 1

media_trabalho = soma_trabalho / n2
media_bimestral = 0.3 * media_trabalho + 0.7 * media_prova

print("Sua média bimestral será de",media_bimestral)

