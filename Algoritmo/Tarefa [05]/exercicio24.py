print("==============================")
inicio = int(input("Informe a hora de inicio: "))
termino = int(input("Informe a hora de término: "))
if inicio < termino:
    duracao = termino - inicio
else:
    duracao = (24 - inicio) + termino
print("A duração do jogo em horas será de " + str(duracao))
print("==============================")