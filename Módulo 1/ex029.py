print("Hello world!")

vel = float(input("Digite a Velocidade que você estava dirigindo: "))

if vel > 80:
    print("Você ultrapassou o Limite de velocidade e tera que pagar {} Reais de multa".format((vel - 80)* 7))
else:
    print("Você estava dirigindo dentro do limite de velocidade!")
