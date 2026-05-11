print("Hello world!")

aux = str(input("Digite uma palavra: ")).upper().strip()

print("A letra A apareceu {} vezes \n Ela apareceu na primeira vez na posição {} \n e apareceu pela ultima vez na posição {} ".format(aux.count('A'), aux.find('A')+1 ,aux.rfind('A')+1 ))
