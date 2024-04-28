print("==============================")
valor = int(input("Informe sua idade: "))
resto = valor % 2
if resto == 0:
    if valor > 0:
        print("O valor é par e positivo")
    elif valor < 0:
        print("O valor é par e negativo")
    else:
        print("O valor é par e neutro")
else:
    if valor > 0:
        print("O valor é ímpar e positivo")
    elif valor < 0:
        print("O valor é ímpar e negativo")
    else:
        print("O valor é ímpar e neutro")
print("==============================")