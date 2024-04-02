kwh = int (input("Digite a quantidade de Kwh consumida: "))
tipo = input("Digite o tipo de instalação (R, C, I): ")

if tipo == "R":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60  
else:
    print("Tipo de instalação inválido")
    exit()
valor = kwh * preco
print(f"Valor a ser pago: {valor:.2f} R$")



