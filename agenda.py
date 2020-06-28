nomes = []
opt = 0
def add_name():
    nome = input('Digite um nome: ')
    nomes.append(nome)
def consultar_nome():
    num = input('Verifique qual posição da lista está o nome: ')
    print(nomes.index(num))
def excluir_nome():
    nome2 = input('Digite o nome que deseja remover: ')
    nomes.remove(nome2)
def see_names():
    print('Agenda')
    print(nomes)
def delete_names():
    print('Agenda zerada!')
    nomes.clear()
def close_agenda():
    print('FIM')
while opt != 6:
    print("\t*** A G E N D A ***")
    print('–'*28)
    print("\t\tOpções")
    print('–'*28)
    print("1 - Cadastrar nome")
    print("2 - Consultar nomes")
    print("3 - Excluir nome")
    print("4 - Listar todos os nomes")
    print("5 - Zerar agenda")
    print("6 - Sair")
    opt = int(input("Digite a opção desejada (1 a 6): "))
    if opt == 1:
        add_name()
    elif opt == 2:
        consultar_nome()
    elif opt == 3:
        excluir_nome()
        print('Nome excluído!')
    elif opt == 4:
        see_names()
    elif opt == 5:
        delete_names()
    elif opt == 6:
        close_agenda()
        break