'''7.	Escreva um programa que leia os 3 ângulos de um triângulo e escreva
 se ele é um ACUTÂNGILO, RETÂNGULO ou OBTUSÂNGULO. Sendo que:
a.	Triângulo retângulo: possui um ângulo reto. (igual a 90 graus);
b.	Triângulo obtusângulo possui um ângulo obtuso (maior que 90 graus);
c.	Triângulo escaleno possui ângulos agudo. (menor que 90 graus);
'''

ang1 = float(input('Digite o primeiro ângulo do triângulo: '))
ang2 = float(input('Digite o segundo ângulo do triângulo: '))
ang3 = float(input('Digite o terceiro ângulo do triângulo: '))
if ang1 == 90 or ang2 == 90 or ang3 == 90:
    print('Triângulo RETÂNGULO')
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print('Triângulo OBTUSÂNGULO')
else:
    print('Triângulo ACUTÂNGILO')




