'''3.	As maçãs custam R$ 0,30 cada se forem compradas menos
 do que uma dúzia, e R$ 0,25 se forem compradas pelo menos 12.
   Escreve um programa que leia o número de maçãs compradas e calcule o
     valor total da compra.'''

macas = int(input('Digite o número de maçãs compradas: '))
if macas < 12:
    valor = macas * 0.30
else:
    valor = macas * 0.25
print(f'O valor total da compra é R$ {valor:.2f}')

