'''Escrever um programa que lê a hora de início e hora de término de um jogo, ambas subdivididas em dois valores distintos: horas e minutos.
 Calcular e escrever a duração do jogo, também em horas e minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que 
 o jogo pode iniciar em um dia e terminar no dia seguinte.'''

inicio_hora = int(input("Informe a hora de início do jogo: "))
inicio_min = int(input("Informe os minutos de início do jogo: "))
fim_hora = int(input("Informe a hora de término do jogo: "))
fim_min = int(input("Informe os minutos de término do jogo: "))
duracao_hora = 0
duracao_min = 0
if inicio_hora > fim_hora:
    duracao_hora = 24 - inicio_hora + fim_hora
    if inicio_min > fim_min:
        duracao_min = 60 - inicio_min + fim_min
        duracao_hora -= 1
    else:
        duracao_min = fim_min - inicio_min
else:
    duracao_hora = fim_hora - inicio_hora
    if inicio_min > fim_min:
        duracao_min = 60 - inicio_min + fim_min
        duracao_hora -= 1
    else:
        duracao_min = fim_min - inicio_min
print(f"A duração do jogo foi de {duracao_hora} horas e {duracao_min} minutos.")


