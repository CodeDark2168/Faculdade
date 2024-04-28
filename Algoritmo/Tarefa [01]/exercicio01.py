# ===== Volume da esfera =====
print("==============================")
raio = float(input("Digite o valor do raio da esfera em metros: "))
area = (4/3) * 3.1415 * (raio**3)
print("O volume da esfere é " + str(round(area, 2)) + "m")
print("==============================")

# ===== Área do cubo =====
lado = float(input("Digite o valor do lado do cubo em metros: "))
area = 6 * (lado**2)
print("A área do cubo é " + str(round(area, 2)) + "m")
print("==============================")

# ===== Área do paralelepípedo =====
altura = float(input("Digite o valor da altura do paralelepípedo em metros: "))
largura = float(input("Digite o valor da largura do paralelepípedo em metros: "))
comprimento = float(input("Digite o valor do comprimento do paralelepípedo em metros: "))
area = 2 * (comprimento * largura + largura * altura + altura * comprimento)
print("A área do paralelepípedo é " + str(round(area, 2)) + "m")
print("==============================")

# ===== Área da esfera =====
raio = float(input("Digite o valor do raio da esfera em metros: "))
area = 4 * 3.1415 * (raio**2)
print("a área da esfere é " + str(round(area, 2)) + "m")
print("==============================")

# ===== Área do cilíndro =====
altura = float(input("Digite o valor da altura do cilíndro em metros: "))
raio = float(input("Digite o valor do raio do cilíndro em metros: "))
area = 2 * 3.1415 * raio * (altura + raio)
print("A área do cilíndro é " + str(round(area, 2)) + "m")
print("==============================")

# ===== Área do cone =====
geratriz = float(input("Digite o valor da geratriz do cone em metros: "))
raio = float(input("Digite o valor do raio do cone em metros: "))
area = 3.1415 * raio * (geratriz + raio)
print("A área do cone é " + str(round(area, 2)) + "m")
print("==============================")
