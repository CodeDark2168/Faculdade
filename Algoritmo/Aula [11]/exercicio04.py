senha = input("Digite uma senha: ")

while senha != "1234":
    print("Senha incorreta!")
    senha = input("Digite a senha: novamente ")

print("Senha correta! Acesso permitido.")

#Esse while irá repetir o input até que a senha 1234 seja digitada, logo depois ele irá mostrar o texto. 