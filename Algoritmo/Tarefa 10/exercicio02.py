array = ["Ana", "Bruno", "Carla", "Daniel", "Eva", "Fábio"]
print(array)

n = int(input("Informe a posição do nome você deseja alterar: "))
nome = input("Informe o novo nome: ")

array[n] = nome
print(array)

print(f"Primeiro contato: {array[0]}\nSegundo contato: {array[len(array)-1]}")