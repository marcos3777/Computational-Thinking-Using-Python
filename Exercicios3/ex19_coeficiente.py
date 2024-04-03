import math
a = int(input("Digite o coeficiente a: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("A equação não possui raízes reais.")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}.")            

