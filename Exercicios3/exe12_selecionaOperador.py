'''Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
 Exiba o resultado da operação solicitada. '''

num1 = int (input("Digite o primeiro número: "))
num2 = int (input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")
if operador == "+":
    print(f"Resultado: {num1 + num2}")
elif operador == "-":
    print(f"Resultado: {num1 - num2}")
elif operador == "*":
    print(f"Resultado: {num1 * num2}")
elif operador == "/":
    print(f"Resultado: {num1 / num2}")
else:

    print("Operador inválido")

