'''1.	Faça um programa que solicite a data de nascimento de uma pessoa e 
informe se ela pode votar ou não.'''

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano

if idade >= 16:
    print('Você pode votar!')
else:
    print('Você não pode votar!')

    