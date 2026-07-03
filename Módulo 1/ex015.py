print("Hello world!")

dias = int(input("Digite quantos dias o carro foi alugado: "))
km = int(input("Digite quantos Km o carro rodou: "))

preco = dias * 60 + km *0.15

print("O preco do aluguel vai ser {}".format(preco))
