j = 1
i=0
nome = []
dist = []


while j == 1:
    nome.append(input(f"Digite o nome do {i+1}º competidor: "))
    if len(nome[i]) >= 3:
        dist.append(sorted([float(input(f"Digite a distância do {i+1}º competidor: ")) for _ in range(5)]))
        
        
    
        
        print(f"O competidor {nome[i]} pulou {dist[i][0]}m, {dist[i][1]}m, {dist[i][2]}m, {dist[i][3]}m e {dist[i][4]}m")
        
        minDist = dist[i].pop(0)
        maxDist = dist[i].pop(-1)
        media = sum(dist[i])/len(dist[i])
        
        print(f"O competidor {nome[i]} melhor pulo foi de {maxDist}m, o pior pulo foi de {minDist}m e a média dos demais pulos foi de {media}m")
        
        i += 1
        j = int(input("Digite 1 para continuar ou 0 para sair: "))
    else:
        print("Nome inválido")
        

print("Fim")        


    
    
    

        
    
    