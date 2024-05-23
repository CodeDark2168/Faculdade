soma_prova = 0
soma_trabalho = 0
quantidade_prova = int(input("Informe a quantidade de provas: "))
quantidade_trabalho = int(input("Informe a quantidade de trabalhos: "))

for i in range(quantidade_prova):
    nota = int(input("Informe a nota: "))
    soma_prova += nota

media_prova = soma_prova / quantidade_prova

for i in range(quantidade_trabalho):
    nota = int(input("Informe a nota: "))
    soma_trabalho += nota

media_trabalho = soma_trabalho / quantidade_trabalho
media_bimestral = 0.3 * media_trabalho + 0.7 * media_prova

print("Sua média bimestral será de",media_bimestral)

