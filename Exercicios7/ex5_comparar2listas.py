#Escreva um programa que compare duas listas. Utilizando operações com
#conjuntos, imprima:
#o os valores comuns às duas listas;
#o os valores que só existem na primeira;
#o os valores que existem apenas na segunda;
#o uma lista com os elementos não repetidos das duas listas;
#o a primeira lista sem os elementos repetidos na segunda;

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string3 = ""
string4 = ""
string5 = ""
string6 = ""
string7 = ""

for i in string1:
    if i in string2:
        string3 += i
    else:
        string4 += i
for i in string2:
    if i in string1:
        string5 += i
    else:
        string6 += i
        
for i in string1:
    if i in string2:
        continue
    else:
        string7 += i
for i in string2:
    if i in string1:
        continue
    else:
        string7 += i
        
print(f"Caracteres comuns: {string3}")
print(f"Caracteres que só existem na primeira: {string4}")
print(f"Caracteres que só existem na segunda: {string5}")
print(f"Caracteres não repetidos: {string7}")
print(f"Caracteres da primeira sem repetidos na segunda: {string4}")

# Output:
# Digite a primeira string: AAACTBF
# Digite a segunda string: CBT
# Caracteres comuns: CBT
# Caracteres que só existem na primeira: AAA
# Caracteres que só existem na segunda:
# Caracteres não repetidos: ACTBF
# Caracteres da primeira sem repetidos na segunda: AAA
#
