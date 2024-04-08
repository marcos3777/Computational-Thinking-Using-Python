#7.	Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. 
#Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

dep_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))
mes = 1
total = 0
while mes <= 24:
    total += dep_inicial
    print("Mês: ", mes, "Valor: ", dep_inicial)
    dep_inicial += dep_inicial * taxa_juros
    mes += 1
print("Total ganho com juros no período: ", dep_inicial - total)

