string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string3 = ""

for i in string1:
    if i in string2:
        continue
    else:
         string3 += i
for i in string2:
    if i in string1:
        continue
    else:
        string3 += i
        
print(f"Caracteres comuns: {string3}")
