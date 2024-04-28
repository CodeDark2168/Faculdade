print("==============================")
tempo = float(input("Informe o tempo de trabalho: "))
idade = int(input("Informe sua idade: "))

if idade > 65 or tempo > 35:
    aposentadoria = "100%"
else:
    aposentadoria = "75%"

print("Terá aposentaria de " + aposentadoria)
print("==============================")