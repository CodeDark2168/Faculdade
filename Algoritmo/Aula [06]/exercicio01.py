print("==============================")
idade = int(input("Informe sua idade: "))
altura = int(input("Informe sua altura em centímetros: "))

if idade > 17:
    if altura > 160:
        bolsa = 1120
    else:
        bolsa = 1410
else:
    bolsa = 1439

print("Você terá direito a uma bolsa de R$" + str(bolsa))
print("==============================")