Palavra = str(input("Digite uma palavra: "))

if Palavra == Palavra[::-1]:
    print(f"{Palavra} é um palindromo")
else:
    print(f"{Palavra} não é um palindromo")