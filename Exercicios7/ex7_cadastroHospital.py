fila = []
atendimento = ""
cadastro = []






def menu():
    print("1 - Entrar na fila de espera")
    print("2 - Chamada para cadastro")
    print("3 - Sair")
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
        cadastro.append(paciente)
        cadastro.append(sintomas)
        cadastro.append(endereco)
        
        atendimento = fila.pop(0)
        print(f"Paciente: {cadastro}")
        print(f"Tipo de Atendimento: {atendimento}")
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
    else:
        print("Opção inválida")
    listarFila()
    op = menu()
    