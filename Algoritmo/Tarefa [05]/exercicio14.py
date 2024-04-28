print("==============================")
codigo = int(input("Informe o código do aluno: "))
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media = nota1*0.3 + nota2*0.3 + nota3*0.4
if media >= 6:
    print("A média do aluno " + str(codigo) + " será de " + str(round(media, 2)) + ", ele foi aprovado")
else:
    print("A média do aluno " + str(codigo) + " será de " + str(round(media, 2)) + ", ele foi reprovado")
print("==============================")