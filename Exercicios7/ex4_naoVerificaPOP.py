#O que acontece quando não verificamos se a lista está vazia antes de
#chamarmos o método pop?

lista = [1, 2, 3]
while lista:
    print(lista.pop())
    

print("Fim")
print(lista.pop())
#recebemos um erro de IndexError, pois a lista está vazia e não podemos retirar elementos de uma lista vazia.