#8. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada
# questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

#Maior e Menor Acerto;

#Total de Alunos que utilizaram o sistema;

#A Média das Notas da Turma.

#Gabarito da Prova:




maiorAcerto = 0
menorAcerto = 10
totalAlunos = 0
mediaNotas = 0
somaNotas = 0
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
j = 1
i = 0
while j == 1:
    totalAlunos += 1
    aluno = []
    for x in range(10):
        aluno.append(input(f"Digite a resposta da {x+1}º questão: ").upper())
    acertos = 0
    for x in range(10):
        if aluno[x] == gabarito[x]:
            acertos += 1
    if acertos > maiorAcerto:
        maiorAcerto = acertos
    if acertos < menorAcerto:
        menorAcerto = acertos
    somaNotas += acertos
    mediaNotas = somaNotas/totalAlunos


