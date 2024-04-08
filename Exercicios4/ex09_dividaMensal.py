#9.	Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
#Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, 
#o total pago e o total de juros pago.

divida = float(input("Digite o valor da dívida: "))
juros = float(input("Digite o juros mensal: "))
pagamento = float(input("Digite o valor mensal a ser pago: "))
mes = 1
total = 0
while divida > 0:
    divida += divida * juros
    divida -= pagamento
    total += pagamento
    mes += 1
print("Total de meses para pagar a dívida: ", mes)
print("Total pago: ", total)
print("Total de juros pago: ", total - divida)


