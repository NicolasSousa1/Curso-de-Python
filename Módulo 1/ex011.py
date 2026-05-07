print("Hello world!")

larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))

area = larg * alt
litros = area / 2

print("a parede tem {} metros de altura e {} metros de largura. sua área é de {} metros quadrados e serão necessarios {} litros de tinta para pintar a parede".format(alt, larg, area, litros))
