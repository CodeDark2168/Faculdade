print("==============================")
total = float(input("Informe o valor do total: "))
serie = input("Informe a série: ")

if serie == "E1":
    if total > 180:
        imposto = total * 0.17
    else:
        imposto = total * 0.14
else:
    if total > 199:
        imposto = total * 0.18
    else:
        imposto = total * 0.16

print("O imposto será de " + str(round(imposto, 2)))
print("==============================")