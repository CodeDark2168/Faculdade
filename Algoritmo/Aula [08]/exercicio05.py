lado_1 = float(input("Informe o primeiro valor: "))
lado_2 = float(input("Informe o segundo valor: "))
lado_3 = float(input("Informe o terceiro valor: "))


if lado_1 > 0 and lado_2 > 0 and lado_3 > 0:
    if lado_2 + lado_3 > lado_1 or lado_3 + lado_1 > lado_2 or lado_2 + lado_1 > lado_3:
        if lado_1 == lado_2 and lado_1 == lado_3:
            print("Triângulo Equilátero")
        elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
            print("Triângulo Escaleno")
        else:
            print("Triângulo Isósceles")
    else:
        print("Não é possivel formar um triângulo com esses valores")
else:
    print("Não é possivel formar um triângulo com esses valores")