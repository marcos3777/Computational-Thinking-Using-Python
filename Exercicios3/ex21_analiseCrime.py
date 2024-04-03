contador = 0
resposta1 = input("Você telefonou para a vítima? ")
if resposta1 == "sim" or resposta1 == "Sim" or resposta1 == "SIM" or resposta1 == "s" or resposta1 == "S":
    contador = 1
elif resposta1 != "não" or resposta1 != "Não" or resposta1 != "NÃO" or resposta1 != "n" or resposta1 != "N":
    contador = 0
else:
    print("Resposta inválida.")
    
resposta2 = input("Você esteve no local do crime? ")
if resposta2 == "sim" or resposta2 == "Sim" or resposta2 == "SIM" or resposta2 == "s" or resposta2 == "S":
    contador += 1
elif resposta2 != "não" or resposta2 != "Não" or resposta2 != "NÃO" or resposta2 != "n" or resposta2 != "N":
    contador += 0
else:
    print("Resposta inválida.")

resposta3 = input("Você mora perto da vítima? ")
if resposta3 == "sim" or resposta3 == "Sim" or resposta3 == "SIM" or resposta3 == "s" or resposta3 == "S":
    contador += 1
elif resposta3 != "não" or resposta3 != "Não" or resposta3 != "NÃO" or resposta3 != "n" or resposta3 != "N":
    contador += 0
else:
    print("Resposta inválida.")

resposta4 = input("Você devia para a vítima? ")
if resposta4 == "sim" or resposta4 == "Sim" or resposta4 == "SIM" or resposta4 == "s" or resposta4 == "S":
    contador += 1
elif resposta4 != "não" or resposta4 != "Não" or resposta4 != "NÃO" or resposta4 != "n" or resposta4 != "N":
    contador += 0
else:
    print("Resposta inválida.")

resposta5 = input("Você já trabalhou com a vítima? ")
if resposta5 == "sim" or resposta5 == "Sim" or resposta5 == "SIM" or resposta5 == "s" or resposta5 == "S":
    contador += 1
elif resposta5 != "não" or resposta5 != "Não" or resposta5 != "NÃO" or resposta5 != "n" or resposta5 != "N":
    contador += 0
else:
    print("Resposta inválida.")

if contador == 2:
    print("Você é suspeito do crime.")
elif contador == 3 or contador == 4:
    print("Você é cúmplice do crime.")
elif contador == 5:
    print("Você é o assassino.")