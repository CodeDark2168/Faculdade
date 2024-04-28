print("==============================")
x1 = float(input("Informe o valor de x1: "))
x2 = float(input("Informe o valor de x2: "))
y1 = float(input("Informe o valor de y1: "))
y2 = float(input("Informe o valor de y2: "))
delta1 = (x2-x1)**2
delta2 = (y2-y1)**2

if delta1 > delta2:
    if x1 > x2:
        alfa = delta1 * x1**2
    else:
        alfa = delta1 * x2**2
else:
    alfa = (delta2-delta1)**2

print("O valor de alfa será " + str(round(alfa, 2)))
print("==============================")