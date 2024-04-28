print("==============================")
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))
if a > b and a > c:
    print("O maior valor é " + str(a))
elif b > a and b > c:
    print("O maior valor é " + str(b))
elif c > a and c > b:
    print("O maior valor é " + str(c))
else:
    print("Não há um valor maior")
print("==============================")