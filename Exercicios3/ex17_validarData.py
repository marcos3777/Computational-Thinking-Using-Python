'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. '''
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)
if mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # ano bissexto
        if dia > 0 and dia <= 29:
            print("Data válida")
        else:
            print("Data inválida")
    else:
        if dia > 0 and dia <= 28:
            print("Data válida")
        else:
            print("Data inválida")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 0 and dia <= 30:
        print("Data válida")
    else:
        print("Data inválida")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 0 and dia <= 31:
        print("Data válida")
    else:
        print("Data inválida")
else:
    print("Data inválida")

