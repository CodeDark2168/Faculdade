print("==============================")
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))
if a > b and a > c:
    print("O maior valor é A")
elif b > a and b > c:
    print("O maior valor é B")
elif c > a and c > b:
    print("O maior valor é C")
else:
    print("Não há um valor maior")
print("==============================")