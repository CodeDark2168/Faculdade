idade = int(input("Informe sua idade: "))
salario = float(input("Informe seu salário: "))

if idade < 30:
    salario *= 1.245
    print("Terá o acréscimo de 24.5% e seu salário será de R$",round(salario,2))
else:
    salario *= 1.335
    print("Terá o acréscimo de 33.5% e seu salário será de R$",round(salario,2))

