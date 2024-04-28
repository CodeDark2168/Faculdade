import math

print("==============================")
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))
if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
    print("Os valores " + str(a) + ", " + str(b) + ", " + str(c) + ", não formam triângulo")
else:
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("A área do triângulo é de " + str(round(area, 2)))
print("==============================")

