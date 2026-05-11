print("Hello world!")

nome = str(input("Digite seu Nome completo:")).strip()

print("Seu primeiro nome é {} \nE seu ultimo nome é {}".format(nome.split()[0], nome.split()[-1]))