print("Hello world!")

sal = float(input("Digite o salario do funcionario: "))
por = float(input("Digite qual a porcentagem de aumento do salário: "))
aumento = sal + (sal * por /100)

print("O salário inial era {}, e com {} porcento de aumento será {}".format(sal, por, aumento))
