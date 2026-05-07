print("Hello world!")

texto = input("Digite algo: ")


print("O tipo primitivo desse valor é ", type(texto)) 
print("Só tem espaços? ", texto.isspace())
print("É um numero? ", texto.isnumeric())
print("É alfabetico? ", texto.isalpha())
print("é alfanumerico? ", texto.isalnum())
print("Está em maiusculo? ", texto.isupper())
print("Está em minusculo? ", texto.islower())
print("Está capitalizada? ", texto.istitle())
