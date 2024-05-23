dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
numero = int(input("Qual dia quer saber? "))

if numero > 7:
    print("Valor inválido")
else:
    print(dias[numero - 1])