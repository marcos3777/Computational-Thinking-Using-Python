#Considere o valor dos vetores abaixo para fazer os próximos exercícios:
#v1 = [45, 89, 32, 12, 33]
#1. Fazer uma Função que retorne o primeiro elemento do vetor.
#2. Fazer um procedimento que exiba somente os números negativos contidos no vetor.
#3. Fazer uma função que retorne a soma dos elementos do vetor.
#4. Fazer uma função que retorne a mediados elementos do vetor.
#5. Fazer um procedimento que exiba na tela os números ímpares contidos no vetor.
#6. Fazer um procedimento que exiba na tela o primeiro e o ultimo elemento do vetor.
#7. Fazer um procedimento que exiba os elementos cujos índices sejam pares.
#8. Fazer uma função que retorne True caso um valor passado por parâmetro exista no vetor, senão
#False.
#9. Fazer um procedimento que ordene os elementos do vetor.


#1. Fazer uma Função que retorne o primeiro elemento do vetor.

v1 = [45, 89, 32, 12, 33]

def primeiroElemento(vetor):
    return vetor[0]

print(primeiroElemento(f"1- Primeiro elemento: {v1}"))

#2. Fazer um procedimento que exiba somente os números negativos contidos no vetor.

def numerosNegativos(vetor):
    for x in vetor:
        if x < 0:
            print(f"2- Numeros negativos: {x}")
            
numerosNegativos(v1)

#3. Fazer uma função que retorne a soma dos elementos do vetor.

def somaElementos(vetor):
    soma = 0
    for x in vetor:
        soma += x
    return soma

print(f"3- Soma dos elementos: {somaElementos(v1)}")

#4. Fazer uma função que retorne a mediados elementos do vetor.

def mediaElementos(vetor):
    soma = 0
    for x in vetor:
        soma += x
    return soma/len(vetor)

print(f"4- Media dos elementos: {mediaElementos(v1)}")

#5. Fazer um procedimento que exiba na tela os números ímpares contidos no vetor.

def numerosImpares(vetor):
    for x in vetor:
        if x % 2 != 0:
            print(f"5- Numeros impares: {x}")
            
numerosImpares(v1)

#6. Fazer um procedimento que exiba na tela o primeiro e o ultimo elemento do vetor.

def primeiroUltimo(vetor):
    print(vetor[0])
    print(vetor[-1])
    
    primeiroUltimo(v1)

#7. Fazer um procedimento que exiba os elementos cujos índices sejam pares.

def elementosIndicesPares(vetor):
    for i in range(len(vetor)):
        if i % 2 == 0:
            print(f"7- Elementos com índices pares: {vetor[i]}")
            
elementosIndicesPares(v1)



#8. Fazer uma função que retorne True caso um valor passado por parâmetro exista no vetor, senão False.

def existeValor(vetor, valor):
    for x in vetor:
        if x == valor:
            return True
    return False

print(existeValor(v1, 12))

#9. Fazer um procedimento que ordene os elementos do vetor.

def ordenaVetor(vetor):
    #vetor.sort()
    #print(vetor)
    if len(vetor) > 1:
        for _ in range(len(vetor)):
                for y in range(len(vetor)-1):
                    if vetor[y] > vetor[y+1]:
                        vetor[y], vetor[y+1] = vetor[y+1], vetor[y]
    print(f"9- Vetor ordenado: {vetor}")
    
ordenaVetor(v1)




