print("Hello world!")

distancia = float(input("Qual a distancia da sua viagem? "))

if distancia > 200:
    print("O preço da sua passagem será {}".format(distancia * 0.45))
else: 
    print("O preço da sua passagem será {}".format(distancia * 0.50))