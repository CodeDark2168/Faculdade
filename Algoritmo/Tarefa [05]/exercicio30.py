print("==============================")
indice = float(input("Informe o índice: "))
if indice >= 0.3:
    print("Suspendam as atividades do grupo 1")
elif indice >= 0.4:
    print("Suspendam as atividades do grupo 1 e 2")
elif indice >= 0.5:
    print("Suspendam as atividades de todos os grupos")
else:
    print("Está adequado")
print("==============================")