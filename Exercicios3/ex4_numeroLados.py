'''4.	Escreva um programa que leia o número de lados de um polígono regular
 e a medida do lado (em cm). Calcular e imprimir o seguinte:
a.	Se o número de lados for igual a 3, escrever TRIÂNGULO e exibir o valor 
de sua área;
b.	Se o número de lados for igual a 4, escrever QUADRADO e exibir o valor 
de sua área.
c.	Se o número de lados for igual a 5, escrever PENTÁGONO.
'''

lados = int(input('Digite o número de lados do polígono: '))
medida = float(input('Digite a medida do lado (em cm): '))
if lados == 3:
    area = (medida ** 2 * 3 ** 0.5) / 4
    print(f'TRIÂNGULO\nÁrea: {area:.2f} cm²')
elif lados == 4:
    area = medida ** 2
    print(f'QUADRADO\nÁrea: {area:.2f} cm²')
elif lados == 5:
    print('PENTÁGONO')
else:
    print('Polígono não identificado')

    


