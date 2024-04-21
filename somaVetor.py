def soma_elementos(v):
    soma = 0
    for i in range(len(v)):
        soma += v[i]
    return soma

def elementos_impares(v):
    temp=[]
    for x in v:
        if x % 2 != 0:
            temp.append(x)
    return temp

def main():
    v = [1, 2, 3, 4, 5]
    print(soma_elementos(v))
    print(elementos_impares(v))
    
if __name__ == "__main__":
    main()
    
    