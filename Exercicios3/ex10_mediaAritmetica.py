'''10.	Escreva um programa que lê um valor I, inteiro positivo e 3 
valores A, B e C. Se o valor de I é par então calcular e imprimir na tela a 
média aritmética de A, B e C. Caso contrário, se I>10 então calcular e 
imprimir a média aritmética e ponderada de A, B e C. Os pesos dos valores 
são respectivamente 2, 3 e 4.'''

I = int(input('Digite um valor inteiro positivo: '))
A = float(input('Digite o valor de A: '))   
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))
if I % 2 == 0:
    media = (A + B + C) / 3
    print(f'Média aritmética: {media:.2f}')
elif I > 10:
    media = (A * 2 + B * 3 + C * 4) / 9
    print(f'Média aritmética ponderada: {media:.2f}')
else:
    pass


