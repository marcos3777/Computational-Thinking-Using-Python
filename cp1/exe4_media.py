'''Escrever um algoritmo que lê as 4 notas obtidas por um aluno. 
Calcular a média ponderada de acordo com a seguinte fórmula: (Nota1 + Nota2 x 2 + Nota3 x 3 + Nota4 x 4) / 10'''

num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
num3 = float(input('Digite a terceira nota: '))
num4 = float(input('Digite a quarta nota: '))

media = (num1 + num2 * 2 + num3 * 3 + num4 * 4) / 10
print(f'A média é {media:.2f}')

