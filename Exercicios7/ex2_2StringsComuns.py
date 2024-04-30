#Escreva um programa que leia duas strings e gere uma terceira com os
#caracteres comuns às duas strings lidas. 1ª string: AAACTBF 2ª string:
#CBT Resultado: CBT A ordem dos caracteres dastring gerada não é
#importante, mas deve conter todas as letras comuns a ambas.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string3 = ""

for i in string1:
    if i in string2:
        string3 += i
        
print(f"Caracteres comuns: {string3}")

