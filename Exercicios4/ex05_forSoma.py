##5.	Escreva um programa que leia dois números. Imprima o resultado da 
#multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e 
#subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de
# dois números como somas sucessivas de um deles. 
#Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
#

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0
for i in range (num2):
    soma += num1
print(soma)

