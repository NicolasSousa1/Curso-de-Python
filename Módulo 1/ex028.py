from random import randint

print("Hello world!")

sort = randint(1,4)

tent = int(input("Digite um numero de 1 a 4: "))

if tent == sort:
    print("Você acertou o Número sorteado Parabéns!")
else:
    print("você errou. O numero sorteado é {}".format(sort))