'''5.	Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo,
 conforme a tabela abaixo. Faça um algoritmo que leia o salário e calcule o novo salário,
   mostrando todas as variações para os cargos e exiba uma observação, 
   “verifique seu novo salário de acordo com o seu cargo”. Se o cargo do funcionário não estiver na tabela, 
   ele deverá, então, receber 40% de aumento. Mostre o salário antigo, os novos salários e a diferença. 

Código	Cargo		Percentual
101		Gerente	10%
102		Engenheiro	20%
103		Técnico	30%
'''

salarioAtual = float(input("Digite o seu salário atual: "))
salarioTecnico =  salarioAtual + salarioAtual * 0.3
salarioEngenheiro = salarioAtual + salarioAtual * 0.2
salarioGerente = salarioAtual + salarioAtual * 0.1
salarioOutros = salarioAtual + salarioAtual * 0.4
print(f"Técnico \nSalário Antigo {salarioAtual} / Salário atual: {salarioTecnico}")
print(f"Engenheiro \nSalário Antigo {salarioAtual} / Salário atual: {salarioEngenheiro}")
print(f"Gerente \nSalário Antigo {salarioAtual} / Salário atual: {salarioGerente}")
print(f"Outros \nSalário Antigo {salarioAtual} / Salário atual: {salarioOutros}")
