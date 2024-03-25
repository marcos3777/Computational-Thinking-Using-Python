'''Faça um programa que solicite dois números para o usuário, sendo o primeiro
 a base e segundo o expoente. Calcule o primeiro número elevado ao segundo número e exiba
   o valor na tela.'''

base = float(input('Digite a base: '))
expoente = float(input('Digite o expoente: '))
resultado = base ** expoente
print(f'{base} elevado a {expoente} é igual a {resultado}')

