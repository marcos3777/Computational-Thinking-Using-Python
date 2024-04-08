#11.	Escreva um programa que leia um número e verifique se é ou não um número primo. 
#Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números
# ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

num = int(input("Digite um número: "))
if num == 0 or num == 1:
    print("Não é primo")
elif num == 2:
    print("É primo")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Não é primo")
            break
    else:
        print("É primo")

