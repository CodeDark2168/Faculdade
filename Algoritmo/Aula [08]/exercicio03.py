valor_1 = float(input("Informe o primeiro valor: "))
valor_2 = float(input("Informe o segundo valor: "))
valor_3 = float(input("Informe o terceiro valor: "))

par_1 = 0
par_2 = 0
par_3 = 0
impar_1 = 0
impar_2 = 0
impar_3 = 0

if valor_1 % 2 == 0:
    par_1 = valor_1
else:
    impar_1 = valor_1

if valor_2 % 2 == 0:
    par_2 = valor_2
else:
    impar_2 = valor_2

if valor_3 % 2 == 0:
    par_3 = valor_3
else:
    impar_3 = valor_3

if par_1 > par_2 and par_1 > par_3:
    print("Maior par:",par_1)
elif par_2 > par_1 and par_2 > par_3:
    print("Maior par:",par_2)
elif par_3 > par_1 and par_3 > par_2:
    print("Maior par:",par_3)
else:
    print("Não há valor par maior")

if impar_1 > impar_2 and impar_1 > impar_3:
    print("Maior impar:",impar_1)
elif impar_2 > impar_1 and impar_2 > impar_3:
    print("Maior impar:",impar_2)
elif impar_3 > impar_1 and impar_3 > impar_2:
    print("Maior impar:",impar_3)
else:
    print("Não há valor ímpar maior")
    