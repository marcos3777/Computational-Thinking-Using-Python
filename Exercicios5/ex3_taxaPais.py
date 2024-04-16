paisA = 80000
paisB = 200000
texaCresA = 0.03
taxaCresB = 0.015
anos = 0
while paisA < paisB:
    paisA = paisA + (paisA * texaCresA)
    paisB = paisB + (paisB * taxaCresB)
    anos = anos + 1
print(anos)
print(f"Pais A: {paisA:.0f}")
print(f"Pais B: {paisB:.0f}")
print("Fim do programa")


#ex4 implementado

paisA = input("Digite a população do país A: ")
paisB = input("Digite a população do país B: ")
taxaA = input("Digite a taxa de crescimento do país A: ")
taxaB = input("Digite a taxa de crescimento do país B: ")
anos = 0
while paisA < paisB:
    paisA = paisA + (paisA * taxaA)
    paisB = paisB + (paisB * taxaB)
    anos = anos + 1     

print(anos)
print(f"Pais A: {paisA:.0f}")
print(f"Pais B: {paisB:.0f}")
print("Fim do programa")
