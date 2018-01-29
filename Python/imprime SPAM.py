print "Este algoritimo escreve a palavra 'SPAM' quantas vezes o usuario determinar."

N = input ("escreva um valor : ")
x = 0
for x in range(0, N):
    if int (x) % 2==0:
        print "spam" + str(x)
