print("==============================")
segundo = int(input("Informe o tempo em segundos: "))
minuto = segundo / 60
hora = minuto / 60
print("O tempo do evento será de " + str(round(hora)) + " horas," + str(round(minuto)) + " minutos," + str(round(segundo)) + " segundo")
print("==============================")