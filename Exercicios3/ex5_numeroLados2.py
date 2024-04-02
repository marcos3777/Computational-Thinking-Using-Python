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

'''5.	Acrescente às seguintes mensagens à solução do exercício anterior
 conforme o caso:
a.	Caso o número de lados seja inferior a 3, escrever NÃO É UM POLÍGONO;
b.	Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO 
IDENTIFICADO;
'''
if lados < 3:
    print('NÃO É UM POLÍGONO')
elif lados > 5:
    print('POLÍGONO NÃO IDENTIFICADO')
else:
    pass



