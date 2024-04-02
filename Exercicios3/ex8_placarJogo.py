'''8.	Desenvolva um programa que receba o placar de um jogo de futebol,
 receba a quantidade de gols de cada time. Depois o programa deverá informar
   se foi empate, vitória do primeiro ou do segundo time.'''

time1 = int(input('Digite a quantidade de gols do primeiro time: '))
time2 = int(input('Digite a quantidade de gols do segundo time: '))
if time1 == time2:
    print('EMPATE')
elif time1 > time2:
    print('VITÓRIA DO PRIMEIRO TIME')
else:
    print('VITÓRIA DO SEGUNDO TIME')

    
        