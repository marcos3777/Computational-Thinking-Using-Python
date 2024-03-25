'''Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar.'''

preco = float(input('Digite o preço da mercadoria: '))
desconto = float(input('Digite o percentual de desconto: '))
valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto
print(f'O desconto foi de R$ {valor_desconto:.2f} e o preço final é R$ {preco_final:.2f}')

