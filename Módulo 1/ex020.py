import random

print("Hello world!")

aluno1 = str(input("Digite o nome de um aluno: "))
aluno2 = str(input("Digite o nome de um aluno: "))
aluno3 = str(input("Digite o nome de um aluno: "))
aluno4 = str(input("Digite o nome de um aluno: "))

Lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(Lista)
print("Os sorteados foram respectivamente ")
print(Lista)