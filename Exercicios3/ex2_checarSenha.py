'''2.	Escreva um programa que verifique a validade de uma senha fornecida
 pelo usuário. A sena válida é “123mudar”. Devem ser impressas as seguintes 
 mensagens:
a.	ACESSO PERMITIDO. Caso a senha seja válida
b.	ACESSO NEGADO. Caso a senha seja inválida.
'''

senha = input('Digite a senha: ')
if senha == '123mudar':
    print('ACESSO PERMITIDO')
else:

    print('ACESSO NEGADO')

    