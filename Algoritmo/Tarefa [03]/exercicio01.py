print("==============================")
velocidadeInicial = int(input("Digite a velocidade inicial em m/s: "))
velocidadeFinal = int(input("Digite a velocidade final em m/s: "))
tempo = int(input("Digite o tempo decorrido em segundos: "))
aceleracao = (velocidadeFinal - velocidadeInicial) / tempo
print("==============================")
print("A aceleração média equivale a " + str(round(aceleracao, 2)) + " m/s.")
print("==============================")
