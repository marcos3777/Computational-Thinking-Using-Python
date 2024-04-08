#3.	Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
# O programa 	deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.

for i in range (10, -1, -1):
    print(i)
print("Fogo!")

#4.	Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, 
#dessa vez, apenas os números ímpares.

num = int(input("Digite um número: "))
for i in range (1, num+1, 2):
    print(i)
print("Fogo!")
