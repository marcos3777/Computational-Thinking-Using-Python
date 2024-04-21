numero = int (input("Digite um número: "))
numero = str(numero)
if numero == numero[::-1]:
    print("O número é um palíndromo")
else:
    print("O número não é um palíndromo")
    
    