print("==============================")
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))
if a < b and b < c:
    print(str(a) + " " + str(b) + " " + str(c))
elif b < c and c < a:
    print(str(b) + " " + str(c) + " " + str(a))
elif c < a and a < b:
    print(str(c) + " " + str(a) + " " + str(b))
elif a < c and c < b:
    print(str(a) + " " + str(c) + " " + str(b))
elif b < a and a < c:
    print(str(b) + " " + str(a) + " " + str(c))
else:
    print(str(c) + " " + str(b) + " " + str(a))
print("==============================")