print("==============================")
salario = float(input("Digite o valor do seu salário: "))
imposto = salario * 0.15
inss = salario * 0.17
total = salario - imposto - inss
print("==============================")
print("Seu salário com o desconto do imposto e INSS ficou R$" + str(round(total , 2)))
print("==============================")
