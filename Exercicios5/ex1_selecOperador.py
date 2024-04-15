import math

print("+ - * /")
operador = input("Digite o operador: ")
print("+ - * /")
num1 = 0
num2 = 0


num1 = float (input("Digite o primeiro número: "))
num2 = float (input("Digite o segundo número: "))
   

    

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    print(num1 / num2)
else:
    print("Operador inválido")
