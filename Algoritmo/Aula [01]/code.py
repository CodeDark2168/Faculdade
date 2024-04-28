#1. Olá, mundo!

print("Hello World!");

#2. Seu nome

nome = input("Digite seu nome: ");
print("Olá," +nome+ "!");

#3. Mensagem Multilinha

print("Espero aprender em Python: ");
print("- Como escrever scripts eficientes.")
print("- Análise de dados.")
print("- Desenvolvimento web.")

#4. Concatenação de Strings

parte1 = "Python é ";
parte2 = "incrível!";
print(parte1 + parte2);

#5. Citação Famosa

print('Albert Einstein uma vez disse: "A imaginação é mais importante que o conhecimento."');

#6. Operações Matemáticas Simples

print("Soma: ", 5 + 3);
print("Subtração: ", 10 - 2);
print("Multiplicação: ", 4 * 2);

#7. Listando Informações

print("Nome: Maria");
print("Idade: 25");
print("Cidade Natal: São Paulo");
print("Linguagem Favorita: Python");

#8. Formatação com .format()

nome = "Maria";
idade = 25;
print("Meu nome é {} e tenho {} anos.".format(nome, idade));

#9. F-Strings

nome = "Maria";
idade = 25;
print(f"Meu nome é {nome} e tenho {idade} anos.");

#10. Tabela de Multiplicação

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print('---')