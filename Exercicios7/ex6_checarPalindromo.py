s = input("Digite o numero a ser verificado, sem espaços: ")
i = 0
f = len(s) - 1
palindromo = True
while i < f:
    if s[i] != s[f]:
        palindromo = False
        break
    i += 1
    f -= 1
    
if palindromo:
    print("É palindromo")
else:
    print("Não é palindromo")
    
    