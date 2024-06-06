letras = []
vogais = []
count = 0

for i in range(10):
    letra = input("Informe uma letra: ")
    letras.append(letra)

for i in letras:
    if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u":
        count += 1
        vogais.append(i)

print("Há",count,"vogais, sendo elas:",vogais)
