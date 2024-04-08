#8.	Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de 
#juros do mês seguinte.

dep_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))
dep_mensal = float(input("Digite o valor depositado mensalmente: "))

mes = 1
total = 0
while mes <= 24:
    total += dep_inicial
    print("Mês: ", mes, "Valor: ", dep_inicial)
    dep_inicial += dep_mensal
    dep_inicial += dep_inicial * taxa_juros
    mes += 1
print("Total ganho com juros no período: ", dep_inicial - total)