'''Faça um programa que solicite a distância percorrida em uma determinada viagem e a 
quantidade de combustível gasto neste percurso. Calcule o consumo do veículo em km/l.'''

distancia = float(input('Digite a distância percorrida (em km): '))
combustivel = float(input('Digite a quantidade de combustível gasta (em litros): '))
consumo = distancia / combustivel
print(f'O consumo do veículo foi de {consumo:.2f} km/l')

