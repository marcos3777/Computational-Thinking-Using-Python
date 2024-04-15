print("Digite todas informações corretamente para sair do programa")

while True:
    nome = input("Digite seu nome: ")
    if len(nome) >= 3:
        print(nome)
        idade = int (input("Digite sua idade: "))
        if idade > 0 or idade < 150:
            print(nome)
            print(idade)
            salario = float (input("Digite seu salário: "))
            if salario > 0:
                print(nome)
                print(idade)
                print(salario)
                sexo = input("Digite seu sexo: ")
                if sexo == "f" or sexo == "m":
                    print(nome)
                    print(idade)
                    print(salario)
                    print(sexo)
                    print("s - solteiro(a) c - casado(a) v - viúvo(a) d - divorciado(a)")
                    estadoCivil = input("Digite seu estado civil:  ")
                    if estadoCivil == "s" or estadoCivil == "c" or estadoCivil == "v" or estadoCivil == "d":
                        print(nome)
                        print(idade)
                        print(salario)
                        print(sexo)
                        print(estadoCivil)
                        break
                    else:
                        print("Estado civil inválido")
                else:
                    print("Sexo inválido")
            else:
                print("Salário inválido")
        else:
            print("Idade inválida")
    else:
        print("Nome inválido")

print("Fim do programa")
            

        