import math


cond=0

while cond==0:


    print("+ - * /")
    operador = input("Digite o operador: ")
    print("+ - * /")
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
    cond = int(input("Digite 0 para continuar ou 1 para sair: "))
