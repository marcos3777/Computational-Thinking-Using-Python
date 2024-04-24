#Considere o valor dos vetores abaixo para fazer os próximos exercícios:
#v1 = [41, 72, 39, 4, 35]
#v2 = [0, 0, 0, 0, 0]
#10. Fazer um procedimento chamado 'copia_vetor(v1, v2)' que copie os elementos do vetor v1 em v2.
#11. Fazer um procedimento chamado 'inverte_vetor(v1, v2)' que copie os elementos invertidos do vetor
#v1 em v2, ou seja, o primeiro elemento de v1 será o último de v2.
#12. Fazer um procedimento chamado 'ordena_vetor_crescente(v)' que ordene de forma crescente o
#vetor passado por parâmetro.
#13. Fazer um procedimento chamado 'ordena_vetor_decrescente(v)' que ordene de forma
#decrescente o vetor passado por parâmetro.
#14. Fazer um procedimento chamado 'ordena_vetor(v, forma)' que baseado na forma ('c' para
#crescente ou 'd' para decrescente) ordene na ordem solicitada.
#15. Fazer um procedimento chamado 'separa_pares_impares(v)' que coloque nas posições mais à
#esquerda os valores pares e mais a diretiaos impares.
#16. Fazer uma função chamada 'conta_acima_media(v) que retorne quantos elementos do vetor estão
#acima da média.
#17. Fazer uma função chamada 'maior_elemento(v)' que retorne o elemento de maior valor do vetor.
#18. Fazer um procedimento chamado ‘preenche_lista(l)’ que preencha uma lista passada por
#parâmetro.
#19. Fazer um procedimento chamado ‘exibe_lista(l)’ que exiba os elementos da lista passada por
#parâmetro.

v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

#10. Fazer um procedimento chamado 'copia_vetor(v1, v2)' que copie os elementos do vetor v1 em v2.

def copia_vetor(v1, v2):
    for x in range(len(v1)):
        v2[x] = v1[x]
    return v2

print(f"10- Vetor copiado: {copia_vetor(v1, v2)}")

#11. Fazer um procedimento chamado 'inverte_vetor(v1, v2)' que copie os elementos invertidos do vetor

def inverte_vetor(v1, v2):
    for x in range(len(v1)):
        v2[x] = v1[-(x+1)]
    return v2

print(f"11- Vetor invertido: {inverte_vetor(v1, v2)}")

#13. Fazer um procedimento chamado 'ordena_vetor_crescente(v)' que ordene de forma crescente o vetor passado por parâmetro.

def ordena_vetor_crescente(v):
    
    for x in range(len(v)):
        for y in range(len(v)):
            if v[x] < v[y]:
                aux = v[x]
                v[x] = v[y]
                v[y] = aux
    return v

print(f"13- Ordem crescente: {ordena_vetor_crescente(v1)}")

def ordena_vetor_decrescente(v):
    
    for x in range(len(v)):
        for y in range(len(v)):
            if v[x] > v[y]:
                aux = v[x]
                v[x] = v[y]
                v[y] = aux
    return v

print(f"13- Ordem decrescente: {ordena_vetor_decrescente(v1)}")

#14. Fazer um procedimento chamado 'ordena_vetor(v, forma)' que baseado na forma ('c' para crescente ou 'd' para decrescente) ordene na ordem solicitada.

def ordena_vetor(v, forma):
    if forma == 'c':
        return ordena_vetor_crescente(v)
    else:
        return ordena_vetor_decrescente(v)
    
print(f"14- Ordem crescente: {ordena_vetor(v1, 'c')}")
print(f"14- Ordem decrescente: {ordena_vetor(v1, 'd')}")

#15. Fazer um procedimento chamado 'separa_pares_impares(v)' que coloque nas posições mais à esquerda os valores pares e mais a diretiaos impares.
 
def separa_pares_impares(v):
    pares = []
    impares = []
    for x in v:
        if x % 2 == 0:
            pares.append(x)
        else:
            impares.append(x)
    return pares + impares

print(f"15- Pares à esquerda e ímpares à direita: {separa_pares_impares(v1)}")

#16. Fazer uma função chamada 'conta_acima_media(v) que retorne quantos elementos do vetor estão acima da média.


def tamanhoVetor(v):
    for x in v:
        x += 1
    return x

def somaVetor(v):
    soma = 0
    for x in v:
        soma += x
    return soma

def conta_acima_media(v):
    media = somaVetor(v)/tamanhoVetor(v)
    acimaMedia = 0
    for x in v:
        if x > media:
            acimaMedia += 1
    return acimaMedia

print(f"16- Acima da média: {conta_acima_media(v1)}")

    
#17. Fazer uma função chamada 'maior_elemento(v)' que retorne o elemento de maior valor do vetor.

def maior_elemento(v):
    maior = 0
    for x in v:
        if x > maior:
            maior = x
    return maior

print(f"17- Maior elemento: {maior_elemento(v1)}")

#18. Fazer um procedimento chamado ‘preenche_lista(l)’ que preencha uma lista passada por parâmetro.

def preenche_lista(v):
    for x in v:
        v[x] = 0
    return v

print(f"18- Lista preenchida: {preenche_lista(v1)}")

#19. Fazer um procedimento chamado ‘exibe_lista(l)’ que exiba os elementos da lista passada por parâmetro.

def exibe_lista(v):
    for x in v:
        print(f"19- Elementos da lista: {v[x]}")
        
        

        
def ordena_crescente(v):
    temp = []
    indice = 0
    tamanho = tamanhoVetor(v)
    while indice < tamanho:
        menor_ = menor(v)
        print (menor_)
        temp.append(menor_[0])
        v.pop(menor_[1])
        indice+=1
    return temp
v1 = [45,89,32,12,33]
print (ordena_crescente(v1))