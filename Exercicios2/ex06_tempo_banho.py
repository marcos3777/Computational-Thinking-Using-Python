'''Escreva um programa que irá solicitar a quantidade de pessoas de uma residência e a
 quantidade de minutos em média que as pessoas se demoram no banho. Sabendo que o chuveiro é de 2400 W,
  o programa deverá calcular e exibir o consumo da energia elétrica, em quilowatt-hora no final do mês 
  (30 dias) e o valor em reais gasto, dado que o valor do KWh é de R$ 0,40.'''

pessoas = int(input("Digite a quantidade de pessoas na residência: "))
tempo = int(input("Digite a quantidade de minutos que as pessoas se demoram no banho: "))
consumo = (2400 * tempo * 30 * pessoas) / 1000
valor = consumo * 0.40
print(f"O consumo de energia elétrica é de: {consumo:.2f} KWh e o valor em reais gasto é de: {valor:.2f} R$")
