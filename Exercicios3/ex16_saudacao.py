'''Escreva um programa que solicite o nome do usuário e apenas dê uma mensagem de acordo com o horário/período (Bom dia, Boa tarde ou Boa noite). '''

nome = input("Digite seu nome: ")
hora = int(input("Digite a hora atual: "))
if hora >= 0 and hora < 12:
    print(f"Bom dia, {nome}")
elif hora >= 12 and hora < 18:
    print(f"Boa tarde, {nome}")
elif hora >= 18 and hora < 24:
    print(f"Boa noite, {nome}")
else:
    print("Hora inválida")
    exit()

    

