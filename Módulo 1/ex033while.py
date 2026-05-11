print("Hello world!")
i = 0
num = [0, 0, 0]
while i < 3:
    num[i] = int(input("Digite um numero:"))
    i += 1
print("o maior número digitado é {}".format(max(num)))
print("o menor número digitado é {}".format(min(num)))