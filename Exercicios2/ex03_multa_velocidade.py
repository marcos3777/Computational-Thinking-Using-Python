#3.	Escreva um programa que pergunte a velocidade 
#do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o 
#usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km/h acima de 80 km/h. 

vel = int(input("Digite a sua velocidade atual: "))

vel = vel // 80
multa = vel % 80

print(f"Vc estava {vel} a cima de 80, sua multa vai ser: {multa}$ reais.")
