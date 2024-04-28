print("==============================")
codigo = int(input("Informe o código do aluno: "))
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
ME = (nota1 + nota2 + nota3)/3
MA = (nota1 + (nota2 * 2) + (nota3 * 3) + ME)/7
if MA > 9:
    print("O aluno",codigo,"ficou com conceito A, com a média dos exercícios de",round(ME, 2),", com a média aritmética de",round(MA, 2),"ta aprovado")
elif MA >= 7.5 and MA <= 9:
    print("O aluno", codigo,"ficou com conceito B, com a média dos exercícios de",round(ME, 2),", com a média aritmética de",round(MA, 2),"ta aprovado")
elif MA >= 6 and MA < 7.5: 
    print("O aluno", codigo,"ficou com conceito C, com a média dos exercícios de",round(ME, 2),", com a média aritmética de",round(MA, 2),"ta aprovado")
elif MA >= 4 and MA < 6: 
    print("O aluno", codigo,"ficou com conceito D, com a média dos exercícios de",round(ME, 2),", com a média aritmética de",round(MA, 2),"ta reprovado")
elif MA < 4: 
    print("O aluno", codigo,"ficou com conceito E, com a média dos exercícios de",round(ME, 2),", com a média aritmética de",round(MA, 2),"ta reprovado")
print("==============================")