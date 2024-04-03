num1 = int(input("Digite um número inteiro: "))
if num1 > 1000:
    print("Número inválido")
else:
    centenas = num1 // 100
    print(f"O número {num1} tem {centenas} centenas.")
    dezenas = num1 % 100
    dezenas = dezenas // 10
    print(f"O número {num1} tem {dezenas} dezenas.")
    unidades = dezenas % 10
    print(f"O número {num1} tem {unidades} unidades.")
    print(f"O número {num1} tem {centenas} centenas, {dezenas} dezenas e {unidades} unidades.")
