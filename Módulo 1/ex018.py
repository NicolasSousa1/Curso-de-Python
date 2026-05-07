from math import radians, sin, cos, tan

print("Hello world!")

angulo = (int(input("Digite um angulo: ")))

radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print("O seno do angulo {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}".format(angulo, seno, cosseno, tangente))