print("Hello world!")

num = int(input("Digite um Numero de 0 a 9999:"))

print(" Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}".format(num // 1 % 10, num //10 % 10, num // 100 % 10, num // 1000 % 10 ))
