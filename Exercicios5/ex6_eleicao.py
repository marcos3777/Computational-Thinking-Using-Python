cond = 0
totalVotes = 0
total1 = 0
total2 = 0
total3 = 0
totalBranco = 0
totalNulo = 0
voto = 1
while voto != 0:
    print("1- Huguinho ")
    print("2- Zezinho")
    print("3- Luizinho")
    print("4- Voto nulo")
    print("5- Voto em branco")
    voto = input("Digite o número do candidato: ")
    if voto == 1:
        print("Huguinho ")
        total1 += total1
    elif voto == 2:
        print("Zezinho")
        total2 += total2
    elif voto == 3:
        print("Luizinho")
        total3 += total3
    elif voto == 4:
        print("Voto em branco")
        totalBranco += totalBranco
    elif voto == 5:
        print("Voto nulo")
        totalNulo += totalNulo


    totalVotes = totalVotes + 1


    #cond = int(input("Digite 0 para continuar ou 1 para sair: "))

    print(f"Total de votos Huginho: {total1}")
    print(f"Total de votos Zezinho: {total2}")
    print(f"Total de votos Luizinho: {total3}")
    print(f"Total de votos em branco: {totalBranco}")
    print(f"Total de votos nulos: {totalNulo}")
    print(f"Total de votos: {totalVotes}")

porcentNulo = (totalNulo / totalVotes) * totalVotes 
porcentBranco = (totalBranco / totalVotes) * totalVotes
porcent1 = (total1 / totalVotes) * totalVotes
porcent2 = (total2 / totalVotes) * totalVotes
porcent3 = (total3 / totalVotes) * totalVotes

print(f"Porcentagem de votos nulos: {porcentNulo:.2f}")
print(f"Porcentagem de votos em branco: {porcentBranco:.2f}")
print(f"Porcentagem de votos Huguinho: {porcent1:.2f}")


