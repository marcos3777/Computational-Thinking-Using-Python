#4.	Escrever um algoritmo que lê o número de identificação, 
#as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios 
#(ME) que fazem parte da avaliação. Calcular a média de aproveitamento (MA), usando a 
#fórmula:
# MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
me = (nota1 + nota2 + nota3) / 3
ma = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7

print(f"A média de aproveitamento é: {ma:.2f}")