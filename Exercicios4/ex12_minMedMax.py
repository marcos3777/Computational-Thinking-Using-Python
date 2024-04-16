#Escreva um programa que solicite ao usuário a quantidade de números que ele deseja inserir, o programa deverá determinar 
# o valor máximo, o valor mínimo e o valor médio de uma sequência de inteiros. sem usar vetor ou lista

num = int(input("Digite a quantidade de números: "))
max = 0
min = 0
soma = 0
for i in range(num):
    num = int(input("Digite um número: "))  # Solicita um número ao usuário a cada iteração
    if i == 0:
        max = num
        min = num
    if num > max:
        max = num
    if num < min:
        min = num
    soma += num
    
print(f"O maior número é {max}")
print(f"O menor número é {min}")
print(f"A média é {soma/num}")

