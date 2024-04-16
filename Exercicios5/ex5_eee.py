#5.	Um funcionário de uma empresa recebe aumento salarial anualmente: 
#Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa 
#permitindo que o usuário digite o salário inicial do funcionário.

salario = 1000
ano = 1995
aumento = 0.015
anoAtual = 2024
while ano < anoAtual:
    ano == 1996
    salario = salario + (salario * aumento)
    aumento = aumento * 2
   
ano = ano + 1
print(f"Salário atual: {salario:.2f}")
print(f"Aumento: {aumento:.2f}")

print(f"Salário atual: {salario:.2f}")
print("Fim do programa")