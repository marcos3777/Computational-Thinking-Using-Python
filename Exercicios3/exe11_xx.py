'''11.	Escreva um programa que determine o valor máximo, o valor 
mínimo e o valor médio de uma sequência de dez números inteiros solicitados
 ao usuário.'''

maximo = 0
minimo = 0
soma = 0
for i in range(10):
    numero = int(input('Digite um número inteiro: '))
    if i == 0:
        maximo = numero
        minimo = numero
    else:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    soma += numero
media = soma / 10
print(f'Valor máximo: {maximo}\nValor mínimo: {minimo}\nValor médio: {media:.2f}')

