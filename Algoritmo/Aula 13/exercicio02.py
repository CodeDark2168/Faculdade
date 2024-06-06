strings = []

for i in range(6):
    string = input(f"Digite a string {i+1}: ")
    strings.append(string)

print("Strings que começam com 'A':")
for string in strings:
    if string.lower().startswith('a'):
        print(string)

# O for pedirá para o usuário digitar 6 string, depois o outro for pegará a primeira letra
# de cada elemento, transformará em minuscula e verificará se começa com A, se sim ele irá mostrar.

print("Strings que terminam com 'A':")
for string in strings:
    if string.lower().endswith('a'):
        print(string)
