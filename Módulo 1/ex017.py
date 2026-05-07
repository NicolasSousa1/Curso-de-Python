from math import hypot

print("Hello world!")

catop = int(input("Digite o valor do cateto oposto: "))
catadj = int(input("Digite o valor do cateto adjacente: "))

'''re = (pow(catop, 2) + pow(catadj, 2))
re = math.sqrt(re)

print("A hipotenusa é {:.2f}".format(re))'''

re = hypot(catop, catadj)

print("A hipotenusa é {:.2f}".format(re))
