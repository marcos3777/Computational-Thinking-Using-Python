#Para os próximos exercícios utilize estas lista para passar como parâmetro:
#Lista1 = [‘eds’, ‘56’, ‘fiap’, ‘ester’, ‘True’, ‘45.78’, ’12’, ’78’]
#Lista2 = [‘alberto’, ‘41’, ‘fiap’, ‘belem’, ‘False’, ‘70.780’, ’18’, ’171’]
#20. Sabemos que a função len() do Python retorna a quantidade de elementos de uma lista. Faça uma 
#função chamada ‘conta_elementos(l)’ que tenha o mesmo efeito, mas percorrendo a lista.,

lista1 = ['eds', '56', 'fiap', 'ester', 'True', '45.78', '12', '78']
lista2 = ['alberto', '41', 'fiap', 'belem', 'False', '70.780', '18', '171']

def conta_elementos(l):
    count = 0
    for i in l:
        count += 1
    return count

print(f"Ex20 - Contador de elementos na lista = {conta_elementos(lista1)}")
print(f"Ex20 - Contador de elementos na lista = {conta_elementos(lista2)}")

#Sabemos que a função index() do Python retorna o índice do elemento passado por parâmetro. 
#Faça uma função parecida chamada ‘retorna_indice(elemento)’ com a melhoria de retornar -1 caso 
#o elemento não seja encontrado.

def retorna_indice(l, elemento):
    for i in range(conta_elementos(l)):
        if l[i] == elemento:
            return i
    return -1



print(f"Ex21 - Retorna indice do elemento na lista1 = {retorna_indice(lista1, '12')}")
print(f"Ex21 - Retorna indice do elemento na lista2 = {retorna_indice(lista2, 'fiap')}")

#Sabemos que a função count() do Python retorna a quantidade de um elemento especifico. Faça 
#uma função chamada ‘busca(l,elemento)’ que tenha o mesmo efeito.

def busca(l, elemento):
    count = 0
    for i in l:
        if i == elemento:
            count += 1
    return count

print(f"Ex22 - Retorna indice do elemento na lista1 = {busca(lista1, '12')}")
print(f"Ex22 - Retorna indice do elemento na lista2 = {busca(lista2, 'fiap')}")

#Fazer uma função chamada ‘conta_inteiro(l)’ que conte quantos elementos inteiros existem em
#uma lista.

def conta_inteiro(l):
    count = 0
    for i in l:
        if i.isdigit():
            count += 1
    return count

print(f"Ex23 - Contador de inteiros na lista1 = {conta_inteiro(lista1)}")
print(f"Ex23 - Contador de inteiros na lista2 = {conta_inteiro(lista2)}")

#Fazer uma função chamada ‘conta_string(l)’ que conte quantos elementos strings existem em uma 
#lista.

def conta_string(l):
    count = 0
    for i in l:
        if i.isalpha():
            count += 1
    return count

print(f"Ex24 - Contador de strings na lista1 = {conta_string(lista1)}")
print(f"Ex24 - Contador de strings na lista2 = {conta_string(lista2)}")

#Fazer uma função chamada ‘conta_boolean(l)’ que conte quantos elementos lógicos existem em 
#uma lista.

def conta_boolean(l):
    count = 0
    for i in l:
        if i == 'True' or i == 'False':
            count += 1
    return count

print(f"Ex25 - Contador de boolean na lista1 = {conta_boolean(lista1)}")
print(f"Ex25 - Contador de boolean na lista2 = {conta_boolean(lista2)}")

#Fazer uma função chamada ‘conta_float(l)’ que conte quantos elementos floatexistem em uma 
#lista

def conta_float(l):
    count = 0
    for i in l:
        if '.' in i:
            count += 1
    return count

print(f"Ex26 - Contador de float na lista1 = {conta_float(lista1)}")
print(f"Ex26 - Contador de float na lista2 = {conta_float(lista2)}")

#Fazer um procedimento chamado ‘copia_int(lista1, lista2)’ que verifique na lista1 se um dado é 
#inteiro e copie para a lista2 este dado convertido em inteiro

def copia_int(lista1, lista2,lista3):
    for i in lista1:
        if i.isdigit():
            lista3.append(int(i))
        
    for i in lista2:
        if i.isdigit():
            lista3.append(int(i))
        
    return lista3

lista3 = []
print(f"Ex27 - Lista copiada de inteiros = {copia_int(lista1,lista2, lista3)}")





