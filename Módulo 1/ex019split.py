import random

print("Hello world!")
lista = ''
ListaSeparada = ''
espaco = ' '
i = 0

while i < 4: 
    alunos = str(input("Digite o nome dos alunos: "))
    lista = lista + espaco + alunos
    i= i + 1


ListaSeparada = lista.split()
print(ListaSeparada)

print("O sorteado foi {}".format(random.choice(ListaSeparada)))
