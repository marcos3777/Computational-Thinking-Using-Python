'''22.	O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
    				Até 5 Kg		Acima de 5 Kg
    File Duplo      	R$ 4,90 por Kg		R$ 5,80 por Kg
    Alcatra           		R$ 5,90 por Kg 		R$ 6,80 por Kg
    Picanha          		R$ 6,90 por Kg 		R$ 7,80 por Kg
 Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites 
 para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o 
 total a compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as
   informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

'''

print("Promoção do Mercado")
print("Escolha o tipo de carne:")
print("1 - File Duplo")
print("2 - Alcatra")
print("3 - Picanha")
tipo = int(input("Digite o número correspondente ao tipo de carne: "))
quantidade = float(input("Digite a quantidade de carne em Kg: "))
if tipo == 1:
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80
    tipo = "File Duplo"
elif tipo == 2:
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80
    tipo = "Alcatra"
elif tipo == 3:
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80
    tipo = "Picanha"
else:
    print("Tipo de carne inválido.")
    preco = 0
print(f"Tipo de carne: {tipo}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço total: R$ {preco:.2f}")
pagamento = input("Digite o tipo de pagamento (cartão Tabajara ou dinheiro): ")
if pagamento == "cartão Tabajara":
    desconto = preco * 0.05
    preco = preco - desconto
    if quantidade > 5:
        print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor a pagar: R$ {preco:.2f}")
else:
    print(f"Valor a pagar: R$ {preco:.2f}")
print("Obrigado por comprar no Hipermercado Tabajara!")

