#11.	Escreva um programa que leia um número e verifique se é ou não um número primo. 
#Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números
# ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
#12.	Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.



#12.	Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

def numPrimo(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Digite um número: "))
    for i in range(1, n+1):
        if numPrimo(i):
            print(i, end=' ')

main()








