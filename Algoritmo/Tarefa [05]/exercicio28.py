print("==============================")
horaI = int(input('Digite a hora inicial: '))
minutoI = int(input('Digite os minutos iniciais: '))

horaF = int(input('Digite a hora final: '))
minutoF = int(input('Digite os minutos finais: '))

tempoI = (horaI * 60) + minutoI
tempoF = (horaF * 60) + minutoF

if horaI == horaF and minutoI == minutoF:
    print('A duração do jogo foi de 24 horas.')
elif tempoI < tempoF:
    duracao = tempoF - tempoI
    hora = duracao/60
    minuto = duracao%60
    print('A duração do jogo foi de', round(hora), 'horas e', minuto, 'minutos.')
else:
    duracao = (24 * 60 - tempoI) + tempoF
    hora = duracao/60
    minuto = duracao%60
    print('A duração do jogo foi de', round(hora), 'horas e', minuto, 'minutos.')
print("==============================")