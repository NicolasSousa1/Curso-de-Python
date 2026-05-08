import random

print("Hello world!")

i = 0
nomes = ['', '', '', '']

while i < 4:
    nomes[i] = str(input("Digite o Nome de um aluno: "))
    i = i + 1

print("O sorteado foi {}".format(random.choice(nomes)))

