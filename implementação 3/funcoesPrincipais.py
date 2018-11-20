"""
Universidade Federal de Pernambuco - UFPE
Centro de Informática
Bacharelado em Sistemas de Informação
IF968 - Programação 01
Autor: (Tomás Nascimento Pimentel Barros)(tnpb)
E-mail: (tnpb@cin.ufpe.br)
"""
import funcoesComplementares as fc


def descriptografarArquivo(nomeArquivo, arquivoDescriptografado):
    """
    @descriptografarArquivo(nomeArquivo)
    essa função tem como objetivo carregar o arquivo "usuarios.txt" e descriptografá-lo, retornando uma lista com os dados
    descriptografados que servirá como parâmetro da função gerarDicionario()
    """
    if nomeArquivo == "usuarios.txt":
        listaCriptograda = fc.formatarArquivo(nomeArquivo)
    else:
        listaCriptograda = fc.formatarELementos(nomeArquivo)

    def conseguirNumerosCripto():
        arquivo = open("private/chavePrivada.txt", "r")
        linha = arquivo.readline()
        arquivo.close()
        d, n = linha.split(" ")
        d, n = int(d), int(n)
        return d, n

    d, n = conseguirNumerosCripto()

    def descriptografarStrings():
        listaDescriptografada = []
        for linha in listaCriptograda:
            stringDescriptografada = ""
            stringTemp = ""
            for caractere in linha:
                if caractere == ",":
                    stringDescriptografada += ","
                elif caractere != " " and caractere != ",":
                    stringTemp += caractere
                else:
                    y = int(stringTemp)
                    x = chr((y ** d) % n)
                    x = str(x)
                    stringDescriptografada += x
                    stringTemp = ""
            stringDescriptografada += "\n"
            listaDescriptografada.append(stringDescriptografada)
        return listaDescriptografada

    def escreverArquivoTemporario():
        # var
        listaDescriptografada = descriptografarStrings()
        # execução
        file = open(arquivoDescriptografado, "w")
        # escrevendo linha por linha
        for linha in listaDescriptografada:
            file.write(linha)
        file.close()

    escreverArquivoTemporario()
    return descriptografarStrings()


def login(dicionarioElementos):
    """
    @login(dicionarioElementos) essa função pede do usuário seu login e senha, checa se eles existem num dicionário que
    armazena o dado de todos os usuários e realiza o login caso o usuário esteja cadastrado
    """
    loginEfetuado = False
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if usuario in dicionarioElementos:
        if senha == dicionarioElementos[usuario][0]:
            print("login efetuado com sucesso! \nSeja bem-vindo %s!" % usuario)
            loginEfetuado = True
        else:
            print("a senha digitada está incorreta!")
    else:
        print("%s não cadastrado!" % usuario)
        return None

    if loginEfetuado:
        usuario = usuario
        senha = dicionarioElementos[usuario][0]
        nivelDeAcesso = dicionarioElementos[usuario][1]
        dadosUsuario = (usuario, senha, nivelDeAcesso)
        return dadosUsuario
    else:
        return None


def criptografarArquivo(nomeArquivo):
    """
    @criptografarArquivo(nomeArquivo) tem como função ler o arquivo dos usuarios que não está criptografado(privado)
    e criptografá-los no arquivo 'usuarios.txt' que será público
    """
    listaDescriptografada = fc.formatarArquivo(nomeArquivo)

    def conseguirNumerosCripto():
        arquivo = open("chavePublica.txt", "r")
        linha = arquivo.readline()
        arquivo.close()
        e, n = linha.split(" ")
        e, n = int(e), int(n)
        return e, n
    e, n = conseguirNumerosCripto()

    def criptografar():
        arquivo = open("usuarios.txt", "w")
        for linha in listaDescriptografada:
            stringCriptografada = ""
            for caractere in linha:
                if caractere != ",":
                    y = (ord(caractere)**e) % n
                    stringCriptografada += str(y) + " "
                else:
                    stringCriptografada += ","
            arquivo.write(stringCriptografada)
            arquivo.write("\n")
        arquivo.close()
    criptografar()


def cadastrarUsuario(dicionarioElementos, nivelAcessoOperador):
    """
    @cadastrarUsuario() pede login e senha do usuário que deseja se cadastrar, checa se o login existe,
    confirma senha e adiciona ao arquivo de usuários não encriptados.
    ATENÇÃO! Essa função não adiciona o adm, uma vez que ele já vem no arquivo
    """
    nivelAcessoOperador = int(nivelAcessoOperador)
    alteracao = "usuario não tinha permissão necessária"
    if nivelAcessoOperador >= 2:
        # upando os dados dos arquivos
        file = open("private/usuariosDescriptografados.txt", "r")
        fileLines = file.readlines()
        file.close()
        # criando o novo usuario
        loginNovoUser = input("digite o login que o novo usuário usuará para logar: ")
        # checando se o login já existe
        if loginNovoUser in dicionarioElementos.keys():
            print("login já existe!")
            print("\nrefaça a operação com outro login")
        else:
            # criando a senha
            senha = input("digite a senha que o novo usuário usará para logar: ")
            senhaConfirmacao = input("digite novamente a senha para confirmar: ")
            while senha != senhaConfirmacao:
                print("senha não confere com confirmação!")
                senha = input("digite a senha que que o usuário usará para logar: ")
                senhaConfirmacao = input("digite novamente a senha para confirmar: ")
            # mexendo no novo arquivo
            notEncrypted = open("private/usuariosDescriptografados.txt", "w")
            novoUser = loginNovoUser + "," + senha + "," + "0" + "\n"
            for line in fileLines:
                notEncrypted.write(line)
            notEncrypted.write(novoUser)
            notEncrypted.close()
            alteracao = loginNovoUser
            print("%s cadastrado com sucesso!" % (loginNovoUser))
    else:
        print("\nVocê não tem o nível de permissão necessária para essa operação")
        print("operação abortada!")
    return alteracao


def alterarNivelUsuario(dicionarioElementos, nivelAcessoOperador):
    """
    @alterarNivelUsuario(dicionarioElementos) altera o nível de poder do usuário se o operador tiver um nível de poder superior ao do usuário que ele quer alterar
    """
    nivelAcessoOperador = int(nivelAcessoOperador)
    if nivelAcessoOperador >= 2:
        # alteração do nível de acesso de outro usuário
        loginSubUser = input("digite o login do usuario que terá nível de acesso alterado: ")
        if loginSubUser not in dicionarioElementos:
            print("%s não foi encontrado no sistema!" % loginSubUser)
            print("\nPor favor refaça a operação.")
        else:
            nivelAcessoSubUser = int(dicionarioElementos[loginSubUser][1])
            if nivelAcessoOperador <= nivelAcessoSubUser:
                print("Você não tem nível de acesso requerido para alterar o nível de acesso do usuário %s" % loginSubUser)
            else:
                novoAcessoSubUser = int(input("Digite o novo nível de acesso do usuário: "))
                print(f"Você tem certeza de que deseja mudar o nível do usuário {loginSubUser} de {nivelAcessoSubUser} ",
                       f"para {novoAcessoSubUser}? ")
                decisao = int(input("Digite 1-Sim ou 0-Não: "))
                while decisao != 0 and decisao != 1:
                    print("Resposta Inválida!")
                    decisao = int(input("Digite 1-Sim ou 0-Não: "))

                # função complementar improvisada
                def modificarArquivo(dicionarioElementos):
                    # estocando os dados do arquivo
                    originalFile = open("private/usuariosDescriptografados.txt", "r")
                    dataFileLines1 = originalFile.readlines()
                    originalFile.close()
                    # mudando os dados do arquivo
                    newFile = open("private/usuariosDescriptografados.txt", "w")
                    linhaProcurada = loginSubUser + ',' + str(dicionarioElementos[loginSubUser][0]) + ',' + dicionarioElementos[loginSubUser][1] + "\n"
                    linhaSubstita = loginSubUser + "," + str(dicionarioElementos[loginSubUser][0]) + "," + str(novoAcessoSubUser) + "\n"
                    for line in dataFileLines1:
                        if line != linhaProcurada:
                            newFile.write(line)
                        else:
                            newFile.write(linhaSubstita)
                    newFile.close()

            if decisao == 1:
                modificarArquivo(dicionarioElementos)
                print(f"Nível de acesso do usuário {loginSubUser} alterado com sucesso!")
                return loginSubUser, novoAcessoSubUser
                del nivelAcessoSubUser
            else:
                print("Operação abortada!")
                return "erro"
    else:
        print("\nVocê não tem permissão necessária para realizar essa operação!")
        print("Operação Abortada!")
        return "erro"


def removerUsuario(dicionarioElementos, nivelAcessoOperador):
    """
    @removerUsuario essa função remove um usuário do sistema, se e somente se o operador tiver as permissões necessárias
    para tal
    """
    nivelAcessoOperador = int(nivelAcessoOperador)
    alteracao = "erro"
    if nivelAcessoOperador >= 2:
        # coletando os dados do usuario a ser removido
        cpfRemovedClient = input("digite o login do usuario que você deseja remover: ")
        if cpfRemovedClient not in dicionarioElementos.keys():
            print(f"login: {cpfRemovedClient} não consta no sistema")
        else:
            nivelAcessoRemovedUsr = int(dicionarioElementos[cpfRemovedClient][1])
            if nivelAcessoRemovedUsr >= nivelAcessoOperador or nivelAcessoOperador < 2:
                print("Você não tem permissão suficiente para remover esse usuário")
            else:
                # confirmação
                print(f"Você quer mesmo deletar {cpfRemovedClient} ?")
                print("Se sim, digite-1 caso contrário, digite-0: ")
                condicao = input()
                if condicao == "1":
                    loginRUser = cpfRemovedClient
                    senhaRUser = dicionarioElementos[cpfRemovedClient][0]
                    nivelRUser = str(nivelAcessoRemovedUsr)
                    # criando linha que iremos procurar no arquivo
                    linhaRuser = loginRUser + "," + senhaRUser + "," + nivelRUser + "\n"
                    # mexendo nos arquivos
                    file = open("private/usuariosDescriptografados.txt", "r")
                    fileDataLines = file.readlines()
                    file.close()
                    # deletando os dados do arquivo
                    notEncryptedFile = open("private/usuariosDescriptografados.txt", "w")
                    for line in fileDataLines:
                        if line != linhaRuser:
                            notEncryptedFile.write(line)
                    notEncryptedFile.close()
                    print(f"{loginRUser} removido com sucesso!")
                    alteracao = loginRUser
                else:
                    print(f"Operação abortada! {cpfRemovedClient} não foi removido.")
    else:
        print("\nVocê não tem o nível de permissão parar realizar essa operação!")
        print("operação abortada!")
    return alteracao


def criptografarElementos(nomeArquivo):
    """
    @criptografarElementos função auxiliar minha que criptografa os elementos e os escreve em elementos.txt
    """
    listaDescriptografada = fc.formatarELementos(nomeArquivo)

    def conseguirNumerosCripto():
        arquivo = open("chavePublica.txt", "r")
        linha = arquivo.readline()
        arquivo.close()
        e, n = linha.split(" ")
        e, n = int(e), int(n)
        return e, n
    e, n = conseguirNumerosCripto()

    def criptografar():
        arquivo = open("elementos.txt", "w")
        for linha in listaDescriptografada:
            stringCriptografada = ""
            for caractere in linha:
                if caractere != ",":
                    y = (ord(caractere)**e) % n
                    stringCriptografada += str(y) + " "
                else:
                    stringCriptografada += ","
            arquivo.write(stringCriptografada)
            arquivo.write("\n")
        arquivo.close()
    criptografar()


def cadastrarCliente(dicionarioClientes):
    """
    @cadastrarClientes função que cadastra novos clientes da padaria no banco do sistema
    """

    alteracao = "erro"
    newClient = True

    print("\nPor favor digite as informações do cliente:\n")
    cpfNewClient = input("Digite o CPF do novo cliente: ")
    if cpfNewClient in dicionarioClientes.keys():
        newClient = False
        print("o PDF deste cliente já está cadastrado!")

    if newClient:
        fnNewClient = input("Digite o primeiro nome do novo cliente: ")
        lnNewClient = input("Digite o último nome do novo cliente: ")
        emailNClient = input("Digite o e-mail do novo cliente: ")
        cepNCLient = input("Digite o CEP do novo cliente: ")
        gastosNClient = input("Digite quanto o cliente gastou na compra: ")

        newClientData = cpfNewClient + "," + fnNewClient + "," + lnNewClient + "," + emailNClient + "," + cepNCLient + "," + gastosNClient + "\n"
        # lendo o arquivo complementar
        uncElementos = open("private/elementosDescriptografados.txt", "r")
        fileDataLines = uncElementos.readlines()
        uncElementos.close()
        # escrevendo o novo cliente
        file = open("private/elementosDescriptografados.txt", "w")
        for line in fileDataLines:
            file.write(line)
        file.write(newClientData)
        file.close()
        print("\nCliente cadastrado com sucesso!")
        alteracao = cpfNewClient
    else:
        print("A operação falhou, usuário já cadastrado!")
    return alteracao


def removerCliente(dicionarioElementos, nivelAcessoOperador):
    """
    @removerCliente função que tem como objetivo remover um cliente do sistema da padaria
    """
    nivelAcessoOperador = int(nivelAcessoOperador)
    alteracao = "erro"
    if nivelAcessoOperador >= 2:
        # coletando os dados do usuario a ser removido
        cpfRemovedClient = input("digite o CPF do cliente que você deseja remover: ")
        if cpfRemovedClient not in dicionarioElementos.keys():
            print(f"CPF: {cpfRemovedClient} não consta no sistema")
        else:
            # confirmação
            print(f"Você quer mesmo deletar {cpfRemovedClient} ?")
            print("Se sim, digite-1 caso contrário, digite-0: ")
            condicao = input()
            if condicao == "1":
                firstName = dicionarioElementos[cpfRemovedClient][0]
                lastName = dicionarioElementos[cpfRemovedClient][1]
                email = dicionarioElementos[cpfRemovedClient][2]
                cep = dicionarioElementos[cpfRemovedClient][3]
                gastoPadaria = dicionarioElementos[cpfRemovedClient][4]
                # criando linha que iremos procurar no arquivo
                linhaRClient = cpfRemovedClient + "," + firstName + "," + lastName + "," + email + "," + cep + "," + gastoPadaria + "\n"
                # mexendo nos arquivos
                file = open("private/elementosDescriptografados.txt", "r")
                fileDataLines = file.readlines()
                file.close()
                # deletando os dados do arquivo
                notEncryptedFile = open("private/elementosDescriptografados.txt", "w")
                for line in fileDataLines:
                    if line != linhaRClient:
                        notEncryptedFile.write(line)
                notEncryptedFile.close()
                print(f"{cpfRemovedClient} removido com sucesso!")
                alteracao = cpfRemovedClient
            else:
                print(f"Operação abortada! {cpfRemovedClient} não foi removido.")
    else:
        print("\nVocê não tem o nível de permissão parar realizar essa operação!")
        print("operação abortada!")
    return alteracao


def buscarCliente(dicionarioElementos):
    """
    @buscarCliente função que busca e imprime informações de um cliente da padaria
    """
    mensagem = """\
    -------------------------------
    Digite:
    1 - buscar cliente pelo CPF
    2 - buscar cliente pelo e-mail
    3 - buscar cliente pelo nome
    -------------------------------
    """
    print(mensagem)
    escolha = input()
    clienteAchado = False
    # buscando o cliente de fato
    # buscando por CPF
    if escolha == '1':
        cpf = input("digite o cpf do cliente: ")
        if cpf in dicionarioElementos.keys():
            clienteAchado = True
            clienteKey = cpf

        if clienteAchado:
            print("\no CPF do cliente foi encontrado no sistema!")
        else:
            print("\nCPF não cadastrado no sistema!")
            return None, None
    # buscando por e-mail
    elif escolha == '2':
        email = input("digite o email cliente: ")
        for keys in dicionarioElementos:
            if dicionarioElementos[keys][2] == email:
                clienteAchado = True
                clienteKey = keys

        if clienteAchado:
            print("\nemail cadastrado no sistema!")
        else:
            print("\no email não está cadastrado no sistema!")
            return None, None
    # buscando pelo nome
    elif escolha == '3':
        firstName = input("Digite o primeiro nome do cliente: ")
        lastName = input("Digite o último nome do cliente: ")
        nomeCompleto = firstName + " " + lastName
        # buscando o nome no dicionario
        for keys in dicionarioElementos:
            fn, ln = dicionarioElementos[keys][0], dicionarioElementos[keys][1]
            fullName = fn + " " + ln
            if nomeCompleto == fullName:
                clienteAchado = True
                clienteKey = keys

    if not clienteAchado:
        print("\nome não cadastrado no sistema!")
        return None, None
    elif clienteAchado:
        print("\nnome cadastrado no sistema!")
        # output
        print(clienteKey)
        cpfCliente = clienteKey
        fnCliente = dicionarioElementos[clienteKey][0]
        lnCliente = dicionarioElementos[clienteKey][1]
        emailCliente = dicionarioElementos[clienteKey][2]
        cepCliente = dicionarioElementos[clienteKey][3]
        gastoCliente = dicionarioElementos[clienteKey][4]
        dadosCliente = (cpfCliente, fnCliente, lnCliente, emailCliente, cepCliente, gastoCliente)
        output = f"""\
                        DADOS DO CLIENTE
        ---------------------------------------------
        CPF: {cpfCliente}
        Primeiro Nome: {fnCliente}
        Último Nome: {lnCliente}
        e-mail: {emailCliente}
        CEP: {cepCliente}
        gastos Totais: R${gastoCliente}
        ---------------------------------------------
        """
        print(output)
        return dadosCliente, clienteAchado
    else:
        print("\nOpção Inválida")
        return None, None


def alterarDadosCliente(dicionarioElementos, nivelAcessoOperador):
    """
    @alterarDadosCliente função que altera alguns dos os dados de um cliente da padaria
    """
    nivelAcessoOperador = int(nivelAcessoOperador)
    alteracao = "erro"
    # busca do cliente
    dadosCliente, clienteAchado = buscarCliente(dicionarioElementos)
    # dados não alterados
    cpf = dadosCliente[0]
    fn = dadosCliente[1]
    ln = dadosCliente[2]
    em = dadosCliente[3]
    cep = dadosCliente[4]
    din = dadosCliente[5]
    # lista com novos dados
    novosDadosClientes = [cpf, fn, ln, em, cep, din]

    oldCliente = cpf + ',' + fn + ',' + ln + ',' + em + ',' + cep + ',' + din + '\n'

    if clienteAchado and nivelAcessoOperador >= 2:
        mensagem = """\
        -------------------------------
        Digite:
        1 - alterar CEP do cliente
        2 - alterar e-mail do cliente
        3 - alterar gastos na padaria
        4 - alterar o primeiro nome
        -------------------------------
        """
        print(mensagem)
        escolha = input()
        # alterar o CEP do cliente
        if escolha == "1":
            alteracao = "CEP"
            newCEP = input("Digite o novo CEP do cliente: ")
            novosDadosClientes[4] = newCEP
            print("CEP do cliente alterado com sucesso!")
        # alterar e-mail do cliente
        elif escolha == "2":
            alteracao = "e-mail"
            newEmail = input("Digite o novo email do cliente: ")
            novosDadosClientes[3] = newEmail
        # alterar o total gasto na padaria
        elif escolha == "3":
            alteracao = "valor gasto pelo cliente"
            newValue = input("Digite o quanto o cliente gastou na padaria: ")
            novosDadosClientes[5] = newValue
        # alterar o primeiro nome
        elif escolha == "4":
            alteracao = "primeiro nome do cliente"
            newFirstName = input("Digite o novo primeiro nome do cliente: ")
            novosDadosClientes[1] = newFirstName
        else:
            print("opção inválida!")

        # dados alterados
        cpf = novosDadosClientes[0]
        fn = novosDadosClientes[1]
        ln = novosDadosClientes[2]
        em = novosDadosClientes[3]
        cep = novosDadosClientes[4]
        din = novosDadosClientes[5]

        cliente = cpf + ',' + fn + ',' + ln + ',' + em + ',' + cep + ',' + din + '\n'
        # alterando o arquivo
        # abrindo o arquivo e salvando as informações dele
        arquivo = open("private/elementosDescriptografados.txt", "r")
        dataLines = arquivo.readlines()
        arquivo.close()
        # escrevendo no arquivo
        arquivo = open("private/elementosDescriptografados.txt", "w")
        for line in dataLines:
            if line != oldCliente:
                arquivo.write(line)
            else:
                arquivo.write(cliente)
        arquivo.close()
        return alteracao, cpf
    elif not clienteAchado:
        print("\no cliente que você procurava não foi encontrado!")
    else:
        print("\nVocê não tem o nível de permissão necessário para essa operação!")


def criarLogUsuario(acao, time):
    """
    @logUsuarios função que escreve os as ações dos usuários dentro do programa no arquivo logs.txt, na minha formatação
    específica
    """
    stringTime = ""
    for caractere in time:
        if caractere != ".":
            stringTime += caractere
        else:
            break

    # formatando a data
    stringData = ''
    for caractere in time:
        if caractere != ' ':
            stringData += caractere
        else:
            break
    listaData = stringData.split('-')
    listaData.reverse()
    data = listaData[0] + '/' + listaData[1] + '/' + listaData[2]

    linha = acao + " " + '|' + data + '!' + ' ' + stringTime + "\n"

    # lendo os logs anteriores
    file = open("logs.txt", "r")
    dataLines = file.readlines()
    file.close()
    # escrever o log
    file = open("logs.txt", "w")
    for line in dataLines:
        file.write(line)
    file.write(linha)
    file.close()


def ordenarClientes(dicionarioElementos):
    """
    @ordenarClientes função que ordena os clientes dentro dos arquivos a partir de seus cpfs em ordem numérica usando bubblesort
    """
    lKey = []
    dicio = dicionarioElementos
    # adicioninando os CPFS à lista
    for key in dicio.keys():
        lKey.append(int(key))
    # ordenando a ordem das chaves por bubbleSort
    lenlKey = len(lKey)
    for i in range(lenlKey):
        for j in range(1, lenlKey):
            if lKey[j] < lKey[j - 1]:
                lKey[j], lKey[j - 1] = lKey[j - 1], lKey[j]
    # escrevendo os dados ordenados no arquivo
    file = open("private/elementosDescriptografados.txt", "w")
    for key in lKey:
        key = str(key)
        linha = key + ',' + dicio[key][0] + ',' + dicio[key][1] + ',' + dicio[key][2] + ',' + dicio[key][3] + ',' + dicio[key][4] + '\n'
        file.write(linha)
    file.close()


def buscarLogUsuario():
    """
    @buscarLogUsuario função que busca o que foi feito no sistema, a partir de um usuário ou de uma data
    """
    def dicionarioLog():
        # pegando os dados do arquivo
        file = open("logs.txt", "r")
        dataLines = file.readlines()
        file.close()
        # var para a criação do dicionario
        dicionarioLog = {}
        # criando o dicionario:
        for line in dataLines:
            stringTemp, stringTemp2, key1, key2 = "", "", "", ""
            for caractere in line:
                if caractere != ';':
                    if caractere != "|" and caractere != '!':
                        stringTemp += caractere
                    if caractere == '|':
                        stringTemp2 = stringTemp
                        stringTemp = ""

                    if caractere == '!':
                        key2 = stringTemp
                        stringTemp2 += ' ' + stringTemp
                        break
                else:
                    key1 = stringTemp
            if key1 not in dicionarioLog.keys() and key2 not in dicionarioLog.keys():
                dicionarioLog[key1], dicionarioLog[key2] = [], []
                dicionarioLog[key1].append(stringTemp2)
                dicionarioLog[key2].append(stringTemp2)
            elif key1 not in dicionarioLog.keys() and key2 in dicionarioLog.keys():
                dicionarioLog[key1] = []
                dicionarioLog[key1].append(stringTemp2)
                dicionarioLog[key2].append(stringTemp2)
            elif key1 in dicionarioLog.keys() and key2 not in dicionarioLog.keys():
                dicionarioLog[key2] = []
                dicionarioLog[key1].append(stringTemp2)
                dicionarioLog[key2].append(stringTemp2)
            else:
                dicionarioLog[key1].append(stringTemp2)
                dicionarioLog[key2].append(stringTemp2)
        return dicionarioLog

    dicionarioLog = dicionarioLog()
    # buscando de fato o usuário ou  a data
    escolha = input("digite 1-Buscar ocorrências no log por Data ou 2-Buscar ocorrências por usuário: ")
    achado = False
    if escolha == '1':
        dataProcurada = input("digite a data sobre a qual você quer informações, no formato dd/mm/aaaa: ")
        if dataProcurada in dicionarioLog.keys():
            key = dataProcurada
            achado = True
    elif escolha == '2':
        loginUsuario = input("digite o login do usuario: ")
        if loginUsuario in dicionarioLog.keys():
            key = loginUsuario
            achado = True
    else:
        print("\na opção escolhida é inválida")

    if achado:
        for chave in dicionarioLog.keys():
            if chave == key:
                tamanhoListaChave = len(dicionarioLog[chave])
                for i in range(tamanhoListaChave):
                    print(f"{chave} : {dicionarioLog[chave][i]}\n")
    else:
        print("login de usuário ou data procurado(a) não foi encontrada(a) no sistema!")
