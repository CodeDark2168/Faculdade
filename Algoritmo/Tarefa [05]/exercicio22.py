print("==============================")
cargo = input("Informe o código do produto: ")
salario = int(input("Informe a qunatidade: "))
if cargo == "Gerente":
    novo_salario = salario + salario*0.1
elif cargo == "Engenheiro":
    novo_salario = salario + salario*0.2
elif cargo == "Técnico":
    novo_salario = salario + salario*0.3
else:
    novo_salario = salario + salario*0.4
diferenca = novo_salario - salario
print("O salário passará de R$" + str(salario) + " para R$" + str(novo_salario) + ", com uma diferença de " + str(diferenca))
print("==============================")