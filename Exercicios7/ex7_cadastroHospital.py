fila = []
atendimento = ""
nome = []
sintomas = []
endereco = []
atendimentoF = []
atendimentoMedico = ["Antonio", "João", "Maria", "Pedro", "Ana"]




def printUsuarios():
    for i in range(len(nome)):
        print(f"Nome: {nome[i]}")
        print(f"Sintomas: {sintomas[i]}")
        print(f"Endereço: {endereco[i]}")
        print(f"Atendimento: {atendimentoF[i]}")
        print(f"Médico: {atendimentoMedico[i]}")
        print("-------------------------------")
        printMedicos()

def printMedicos(i):
    if atendimentoF[i] == "G":
        print(f"Médico: {atendimentoMedico[0]}")
    elif atendimentoF[i] == "O":
        print(f"Médico: {atendimentoMedico[1]}")
    elif atendimentoF[i] == "C":
        print(f"Médico: {atendimentoMedico[2]}")
    elif atendimentoF[i] == "P":
        print(f"Médico: {atendimentoMedico[3]}")
    elif atendimentoF[i] == "F":
        print(f"Médico: {atendimentoMedico[4]}")
    else:
        print("Médico não encontrado")
    return

def cadastrarMedico():
    print("Médicos disponíveis: ")
    print("1 - Antonio - G Clínico Geral")
    print("2 - João - O ortopedia")
    print("3 - Maria - C cardiologia")
    print("4 - Pedro - P pediatra")
    print("5 - Ana - F oftalmologia")
    print("6 - Sair")
    print("Digite o atendimentoMedico que deseja alterar: ")
    if op == "1":
        atendimentoMedico[0] = input("Digite o nome do novo médico: ")
    elif op == "2":
        atendimentoMedico[1] = input("Digite o nome do novo médico: ")
    elif op == "3":
        atendimentoMedico[2] = input("Digite o nome do novo médico: ")
    elif op == "4":
        atendimentoMedico[3] = input("Digite o nome do novo médico: ")
    elif op == "5":
        atendimentoMedico[4] = input("Digite o nome do novo médico: ")
    elif op == "6":
        return
    else:
        print("Opção inválida")
    return op

def menu():
    print("1 - Entrar na fila de espera")
    print("2 - Chamada para cadastro")
    print("3 - Listar pacientes")
    print("4 - Cadastrar médico")
    print(" - Sair")
    op = input("Digite a opção desejada: ")
    return op

def adicionarFila():
    tipo = input("G Clínico Geral, O ortopedia, C cardiologia, P pediatra, F oftalmologia: ")
    fila.append(tipo)
        
def chamarCadastro():
    if fila:
        paciente = input("Digite o nome do paciente: ")
        sintomas = input("Digite os sintomas do paciente: ")
        endereco = input("Digite o endereço do paciente: ")        
        nome.append(paciente)
        sintomas.append(sintomas)
        endereco.append(endereco)
        
        atendimento = fila.pop(0)
        atendimentoF.append(atendimento)
        print(f"Paciente: {nome[0]}")
        print(f"Tipo de Atendimento: {atendimentoF}")
    else:
        print("Fila vazia")
        
def listarFila():
    print(f"Fila de espera: {fila}")
        
op = menu()

while op != "3":
    if op == "1":
       adicionarFila() 
    elif op == "2":
        chamarCadastro()
    elif op == "3":
        printUsuarios()
    elif op == "4":
        cadastrarMedico()
    else:
        print("Opção inválida")
    listarFila()
    op = menu()
    