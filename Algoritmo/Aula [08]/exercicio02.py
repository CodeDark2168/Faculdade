ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))

idade_ano = ano_atual - ano_nascimento
idade_hora = (idade_ano * 356) * 24
idade_minuto = idade_hora * 60
idade_semana = (idade_ano * 356) / 7

print("Sua idade de",idade_ano,"anos,",idade_hora,"horas,",idade_minuto,"minutos e",round(idade_semana),"semanas")