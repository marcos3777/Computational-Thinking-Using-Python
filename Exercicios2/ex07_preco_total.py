'''7.	Um vendedor necessita de um programa que calcule o preço total devido por um cliente. 
O algoritmo deve receber o código de um produto e a quantidade comprada e calcular o preço total, 
acrescendo o imposto que varia o seu percentual de acordo com o produto, usando a tabela abaixo:

Código do Produto	Preço unitário		Percentual de imposto
1001			5,32			18%
1324			6,45			18%
6548			2,37			6%
0987			5,32			6%
7623			6,45			12%

O programa devera exibir a saída com o valor pago por cada produto, valor do imposto, imposto total e valor 
total a ser pago.
'''
codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade comprada do produto 1001 : "))
quantidade2 = int(input("Digite a quantidade comprada do produto 1324 : "))
quantidade3 = int(input("Digite a quantidade comprada do produto 6548 : "))
quantidade4 = int(input("Digite a quantidade comprada do produto 0987 : "))
quantidade5 = int(input("Digite a quantidade comprada do produto 7623 : "))

preco = 5.32
imposto = 0.18
valorImposto = 0
valor = preco * quantidade
valorImposto = valor * imposto
valorTotal = valor + valorImposto
print(f"Valor do produto 1001 : {valor:.2f} R$")
print(f"Valor do imposto 1001 : {valorImposto:.2f} R$")
print(f"Valor total: {valorTotal:.2f} R$")

preco2 = 6.45
imposto = 0.18
valorImposto = 0
valor = preco2 * quantidade2
valorImposto = valor * imposto
valorTotal = valor + valorImposto
print(f"Valor do produto 1324 : {valor:.2f} R$")
print(f"Valor do imposto 1324 : {valorImposto:.2f} R$")
print(f"Valor total: {valorTotal:.2f} R$")

preco3 = 2.37
imposto = 0.06
valorImposto = 0
valor = preco3 * quantidade3
valorImposto = valor * imposto
valorTotal = valor + valorImposto
print(f"Valor do produto 6548 : {valor:.2f} R$")
print(f"Valor do imposto 6548 : {valorImposto:.2f} R$")
print(f"Valor total: {valorTotal:.2f} R$")

preco4 = 5.32
imposto = 0.06
valorImposto = 0
valor = preco4 * quantidade4
valorImposto = valor * imposto
valorTotal = valor + valorImposto
print(f"Valor do produto 0987 : {valor:.2f} R$")
print(f"Valor do imposto 0987 : {valorImposto:.2f} R$")
print(f"Valor total: {valorTotal:.2f} R$")

preco5 = 6.45
imposto = 0.12
valorImposto = 0
valor = preco5 * quantidade5
valorImposto = valor * imposto
valorTotal = valor + valorImposto
print(f"Valor do produto 7623 : {valor:.2f} R$")
print(f"Valor do imposto 7623 : {valorImposto:.2f} R$")
print(f"Valor total: {valorTotal:.2f} R$")