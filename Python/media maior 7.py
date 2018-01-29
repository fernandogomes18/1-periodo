# Calcular m�dia maior que 7.

n= int(input('digite a quantidade de alunos' ))
    
soma=0
i=1
while i<=n:
    nota1=float(input('digite  a primeira nota'))
    nota2=float(input('digite a segunda nota'))
    media=(nota1+nota2)/2
    if media > 7.0:
        soma=soma+1
   5 i=i+1   
print soma


