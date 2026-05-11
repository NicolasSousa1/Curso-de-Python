print("Hello world!")

num = int(input("Digite um Número: "))
quoc = num // 2
print(quoc)
resto = num - quoc * 2

if resto == 0:
    print("{} É um numero par".format(num))
else:
    print("{} é um número impar".format(num))
