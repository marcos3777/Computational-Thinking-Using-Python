valor = float(input("Digite o valor do produto: "))
if valor < 20 and valor > 0:
    novoValor = valor * (45/100)
elif valor >= 20:
    novoValor = valor * (30/100)
else:
    print("Valor inválido")
    exit()
    
print(f"O valor do produto foi de {valor} e agora é de {novoValor:.2f}")