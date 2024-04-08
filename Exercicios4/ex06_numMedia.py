#6.	Escreva um programa que solicite números inteiros para o usuário. O programa deve ler os
# números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números 
#digitados, assim como a soma e a média aritmética.

soma = 0
cont = 0
num = 1
while num != 0:
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
print("Quantidade de números digitados: ", cont)
print("Soma dos números digitados: ", soma)
print("Média dos números digitados: ", soma/(cont-1))





