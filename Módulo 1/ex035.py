print("Hello world!")

lado1 = int(input("Digite o tamanho de um lado do triângulo: "))
lado2 = int(input("Digite o tamanho de um lado do triângulo: "))
lado3 = int(input("Digite o tamanho do ultimo lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado3 + lado2 > lado1):
    print("É possível formar um triângulo com essas medidas")
else:
    print("Não é possível formar um triângulo com essas medidas")
