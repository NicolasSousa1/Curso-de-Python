print("Hello world!")

sal = float(input("Digite o seu salário: "))

if (sal > 1250):
    print(f"O seu salário de {sal} terá um aumento de 10% e passará a ser {sal + (sal * 10 /100)}")
else:
    print(f"O seu salário de {sal} terá um aumento de 15% e passará a ser {sal + (sal * 15/100)}")
