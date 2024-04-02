'''6.	Escreva um programa que leia as medidas dos lados de um triângulo e
 escreva se ele é um EQUILÁTERO, ISÓSCELE ou ESCALENO. Sendo que:
a.	Triângulo equilátero: três lados iguais;
b.	Triângulo isóscele possui 2 lados iguais;
c.	Triângulo escaleno possui 3 lados diferentes;
'''

lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))
if lado1 == lado2 == lado3:
    print('Triângulo EQUILÁTERO')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo ISÓSCELES')
else:
    print('Triângulo ESCALENO')

    
