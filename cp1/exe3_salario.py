'''Faça um programa que solicite o salário do usuário e calcule o novo salário com o aumento de 18%.
 O programa deverá exibir o valor do aumento e o novo salário.'''

salario = float(input('Digite o salário: '))
aumento = salario * 0.18
novo_salario = salario + aumento
print(f'O aumento foi de R$ {aumento:.2f} e o novo salário é R$ {novo_salario:.2f}')

