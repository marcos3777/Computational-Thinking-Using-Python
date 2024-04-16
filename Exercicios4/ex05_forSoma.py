'''5.	Escreva um programa que leia dois números. Imprima o resultado da 
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e 
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de
 dois números como somas sucessivas de um deles. 
o print precisa sair assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''


num1 = int(input("Digite o multiplicando: "))
num2 = int(input("Digite o multiplicador: "))

resultado = 0

for i in range(num2):
  resultado += num1

print(f"{num1} × {num2} = ", end="")
for i in range(num2):
  if i == 0:
    print(f"{num1}", end="")
  else:
    print(f" + {num1}", end="")
print(f" = {resultado}")

resultado = 0

for i in range(num1):
    resultado += num2
    
print(f"{num2} × {num1} = ", end="")
for i in range(num1):
    if i == 0:
        print(f"{num2}", end="")
    else:
        print(f" + {num2}", end="")
print(f" = {resultado}")
