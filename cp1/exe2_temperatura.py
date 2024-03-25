'''Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius.'''

fah = float(input('Digite a temperatura em Fahrenheit: '))
cel = (fah - 32) * 5/9
print(f'A temperatura em Celsius é {cel:.2f}')

