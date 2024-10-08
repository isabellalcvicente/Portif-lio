# RODAR NO COLAB
#from google.colab import output


class NovoCarro:
    def __init__(this, codigo, nome, ano, marca, status):
        this.codigo = codigo
        this.nome = nome
        this.ano = ano
        this.marca = marca
        this.status = status

    def __str__(this):
        return "\nCodigo {} \nNome {} \nMarca {} \nAno {} \nStatus {}".format(
            this.codigo, this.nome, this.marca, this.ano, this.status
        )


class NovoCliente:
    def __init__(this, nome, endereco, cpf, email, telefone, infoadc):
        this.nome = nome
        this.endereco = endereco
        this.cpf = cpf
        this.email = email
        this.telefone = telefone
        this.infoadc = infoadc

    def __str__(this):
        return "\nNome: {} \nEndereço: {} \nCPF: {} \nE-mail: {} \nTelefone {}\nInformações Adicionais: {}".format(
            this.nome, this.endereco, this.cpf, this.email, this.telefone, this.infoadc
        )


CarrosCadastrados = []
ClientesCadastrados = []
NewCode = 0


def CadastroClientes():
    global ClientesCadastrados
    InputNomeC = str(input("Digite seu nome: "))
    InputEndereco = str(
        input(
            "Digite seu endereco completo(rua, número, complemento, cep, bairro, cidade, estado): "
        )
    )
    InputCPF = int(input("Digite seu CPF: "))
    InputEmail = str(input("Digite seu E-mail: "))
    InputTelefone = int(input("Digite seu telefone: "))
    InputInfoAdc = str(
        input(
            "Digite suas informações adicionais (caso não hajam informações adicionais, digite '0'): "
        )
    )
    #output.clear()

    if InputInfoAdc == 0:
        InputInfoAdc = "Não há informações adicionais."

    cliente = NovoCliente(
        InputNomeC, InputEndereco, InputCPF, InputEmail, InputTelefone, InputInfoAdc
    )
    ClientesCadastrados.append(cliente)


def VerificaCodigo(codigo):
    global NewCode
    NewCode = codigo
    for i in range(len(CarrosCadastrados)):
        if NewCode == CarrosCadastrados[i].codigo:
            NewCode = int(
                input(
                    "O codigo digitado ja foi cadastrado no carro {}\n{}\n. Digite o codigo novamente: ".format(
                        CarrosCadastrados[i].codigo, CarrosCadastrados[i]
                    )
                )
            )
            #output.clear()
            VerificaCodigo(NewCode)
    return NewCode


def cadastro():
    global NewCode
    print("-------------------CADASTRO DE CARROS--------------------\n")
    InputCodigo = int(input("\nDigite o código: "))
    InputNome = str(input("\nDigite o nome do carro: "))
    InputMarca = str(input("\nDigite a marca do carro: "))
    InputAno = int(input("\nDigite o ano do carro: "))
    InputSituacao = int(
        input("\nDigite a situação atual do carro: 1 - Disponivel; 0 - Indisponivel ")
    )
    #output.clear()
    VerificaCodigo(InputCodigo)

    if InputSituacao == 1:
        InputSituacao = "Disponivel"

    elif InputSituacao == 0:
        InputSituacao == "Indisponivel"

    carro = NovoCarro(NewCode, InputNome, InputAno, InputMarca, InputSituacao)
    CarrosCadastrados.append(carro)
    print("\nCarro com as seguintes informações, está cadastrado:", carro)
    input("\nPressione Enter para continuar.")
    #output.clear()


def busca():
    esc_possiveis = [1, 2, 3, 4, 5]
    esc = int(
        input(
            "Selecione o meio de busca:\n1 - Código\n2 - Nome\n3 - Ano\n4 - Marca\n5 - Status\n"
        )
    )
    atributos = ["codigo", "nome", "ano", "marca", "status"]
    VarAtributo = atributos[esc - 1]  #
    varBusca = [int, str, int, str, str]
    #output.clear()
    if esc in esc_possiveis:
        busca = varBusca[esc - 1](
            input("Digite o {} do carro que deseja buscar: ".format(VarAtributo))
        )
        for i in range(0, len(CarrosCadastrados)):
            if getattr(CarrosCadastrados[i], VarAtributo) == busca:
                print(CarrosCadastrados[i])


def locacao():
    CadastroClientes()
    codigo = int(input("Digite o código do carro: "))
    for i in range(len(CarrosCadastrados)):
        carro_codigo = CarrosCadastrados[i].codigo
        if carro_codigo == codigo:
            if CarrosCadastrados[i].status == "Disponivel":
                print(CarrosCadastrados[i])
                confirma = str(input("\n Esse é o carro que você procura?"))
                if confirma == "sim":
                    CarrosCadastrados[i].status = "Indisponivel"
                    input(
                        "Carro alugado com sucesso.\n\nPressione Enter para continuar. "
                    )
                    #output.clear()
            elif CarrosCadastrados[i].status == "Indisponivel":
                print("Este carro está indisponível")
                input("Pressione Enter para continuar. ")
                #output.clear()


def listagem():
    print("Para ver a lista de carros disponíveis ou emprestados, digite 1 ou 2: \n")
    listagem = int(input("1 - Carros Emprestados\n2 - Carros Disponiveis\n"))
    #output.clear()
    if listagem == 1:
        print("Aqui está a lista de carros emprestados: \n")
        for i in range(len(CarrosCadastrados)):
            if CarrosCadastrados[i].status == "Indisponivel":
                print(CarrosCadastrados[i], "\n")
        input("Pressione Enter para continuar. ")
        #output.clear()

    if listagem == 2:
        print("Aqui está a lista de carros disponíveis para empréstimo: \n")
        for i in range(len(CarrosCadastrados)):
            if CarrosCadastrados[i].status == "Disponivel":
                print(CarrosCadastrados[i], "\n")
        input("Pressione Enter para continuar. ")
        #output.clear()


esc_possiveis = [1, 2, 3, 4]
opcoes = [cadastro, busca, locacao, listagem]
esc = int(
    input(
        "1 - Cadastrar carro\n2 - Consultar Carros \n3 - Emprestar carro \n4 - Lista de Carros Emprestados ou disponiveis \n5 - Sair\n"
    )
)
#output.clear()

while esc in esc_possiveis:
    opcoes[esc - 1]()
    esc = int(
        input(
            "1 - Cadastrar carro\n2 - Consultar Carros \n3 - Emprestar carro \n4 - Lista de Carros Emprestados ou disponiveis \n5 - Sair\n"
        )
    )
    #output.clear()
