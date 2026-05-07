print("Hello world!")

preco = float(input("Digite o valor do produto: "))
desc = float(input("Digite qual a porcentagem de desconto que você deseja: "))

vd = preco*desc /100

print("O valor do produto é {} e com {} porcento de desconto fica {}".format(preco, desc, preco - vd))
