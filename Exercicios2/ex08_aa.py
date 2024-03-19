'''8.	Escrever um algoritmo que lê valor da leitura de consumo de água da residência 
expresso em metros cúbicos. O Programa deverá calcular o valor final da conta de água e esgoto de 
acordo com a seguinte tabela de consumo:

Faixa	Faixas de consumo metros cúbicos	Tarifa por metro cúbico
A	Até 10	R$ 5,50
B	Entre 11 e 20	R$ 0,85
C	Entre 21 e 50	R$ 2,13
D	Acima de 50	R$ 2,36

O valor cobrado do esgoto é o mesmo da água.
Segue um exemplo de saída formatada que o programa deverá exibir:

Leitura: 134 metros cúbicos gastos.

Faixa	Faixas de consumo metros cúbicos	Consumo na Tarifa
A	Até 10	R$ 22,00
B	Entre 11 e 20	R$ 0,00
C	Entre 21 e 50	R$ 63,90
D	Acima de 50	R$ 236,00
		
Valor de água	R$ 321,90
Valor de esgoto	R$ 321,90
Total	R$ 643,80
'''

consumo = int(input("Informe o consumo de água em metros cúbicos: "))
faixa10 = consumo % 10
resto = consumo // 10
consumoTotal = faixa10 * 5.5
print(consumoTotal)
faixa20 = (consumo - faixa10) % 10
print(faixa20)
consumoTotal += (faixa20 * 0.85)
print(consumoTotal)
faixa50 = (consumo - faixa10 - faixa20) // 30
print(faixa50)
