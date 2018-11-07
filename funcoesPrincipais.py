"""
Universidade Federal de Pernambuco - UFPE
Centro de Informática
Bacharelado em Sistemas de Informação
IF968 - Programação 01
Autor: (Tomás Nascimento Pimentel Barros)(tnpb)
E-mail: (tnpb@cin.ufpe.br)
"""
import funcoesComplementares as fc
"""
@descriptografarArquivo(nomeArquivo)
essa função tem como objetivo carregar o arquivo "usuarios.txt" e descriptografá-lo, retornando uma lista com os dados
descriptografados que servirá como parâmetro da função gerarDicionario()
"""


def descriptografarArquivo(nomeArquivo):
    listaCriptograda = fc.formatarArquivo(nomeArquivo)

    def conseguirNumerosCripto():
        arquivo = open("chavePrivada.txt", "r")
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
            listaDescriptografada.append(stringDescriptografada)
        return listaDescriptografada
    return descriptografarStrings()


"""
@login(dicionarioUsers) essa função pede do usuário seu login e senha, checa se eles existem num dicionário que
armazena o dado de todos os usuários e realiza o login caso o usuário esteja cadastrado
"""


def login(dicionarioUsers):
    loginEfetuado = False
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if usuario in dicionarioUsers:
        if senha == dicionarioUsers[usuario][0]:
            print("login efetuado com sucesso! \nSeja bem-vindo %s!" % usuario)
            loginEfetuado = True
        else:
            print("a senha digitada está incorreta!")
    else:
        print("%s não cadastrado!" % usuario)

    if loginEfetuado:
        usuario = usuario
        senha = dicionarioUsers[usuario][0]
        nivelDeAcesso = dicionarioUsers[usuario][1]
        dadosUsuario = (usuario, senha, nivelDeAcesso)
        return dadosUsuario


"""
@criptografarArquivo(nomeArquivo) tem como função ler o arquivo dos usuarios que não está criptografado(privado)
e criptografá-los no arquivo 'usuarios.txt' que será público
"""


def criptografarArquivo(nomeArquivo):
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


"""
@cadastrarUsuario() pede login e senha do usuário que deseja se cadastrar, checa se o login existe,
confirma senha e adiciona ao arquivo de usuários não encriptados.
"""


def cadastrarUsuario(dicionarioUsers):
    # upando os dados dos arquivos
    file = open("usuariosDescriptografados.txt", "r")
    fileLines = file.readlines()
    file.close()
    # criando o novo usuario
    loginNovoUser = input("digite o login que você usuará para logar:")
    # checando se o login já existe
    if loginNovoUser in dicionarioUsers.keys():
        print("login já existe!")
        print("\nrefaça a operação com outro login")
    else:
        # criando a senha
        senha = input("digite a senha que você usará para logar: ")
        senhaConfirmacao = input("digite novamente sua senha para confirmar: ")
        while senha != senhaConfirmacao:
            print("senha não confere com confirmação!")
            senha = input("digite a senha que você usará para logar: ")
            senhaConfirmacao = input("digite novamente sua senha para confirmar: ")
        # mexendo no novo arquivo
        notEncrypted = open("usuariosDescriptografados.txt", "w")
        novoUser = loginNovoUser + "," + senha + "," + "0" + "\n"
        for line in fileLines:
            notEncrypted.write(line)
        notEncrypted.write(novoUser)
        notEncrypted.close()

        print("%s cadastrado com sucesso!" % (loginNovoUser))


"""
@alterarNivelUsuario(dicionarioUsers) altera o nível de poder do usuário se o operador tiver um nível de poder superior ao do usuário que ele quer alterar
"""


def alterarNivelUsuario(dicionarioUsers):
    # identificação do operador
    dadosOperador = login(dicionarioUsers)
    nivelAcessoOperador = int(dadosOperador[2])
    # alteração do nível de acesso de outro usuário
    loginSubUser = input("digite o login do usuario que terá nível de acesso alterado: ")
    if loginSubUser not in dicionarioUsers:
        print("%s não foi encontrado no sistema!" % loginSubUser)
        print("\nPor favor refaça a operação.")
    else:
        nivelAcessoSubUser = int(dicionarioUsers[loginSubUser][1])
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
            def modificarArquivo(dicionarioUsers):
                # estocando os dados do arquivo
                originalFile = open("usuariosDescriptografados.txt", "r")
                dataFileLines1 = originalFile.readlines()
                originalFile.close()
                # mudando os dados do arquivo
                newFile = open("usuariosDescriptografados.txt", "w")
                linhaProcurada = loginSubUser + ',' + str(dicionarioUsers[loginSubUser][0]) + ',' + dicionarioUsers[loginSubUser][1] + "\n"
                linhaSubstita = loginSubUser + "," + str(dicionarioUsers[loginSubUser][0]) + "," + str(novoAcessoSubUser) + "\n"
                for line in dataFileLines1:
                    if line != linhaProcurada:
                        newFile.write(line)
                    else:
                        newFile.write(linhaSubstita)
                newFile.close()

            if decisao == 1:
                modificarArquivo(dicionarioUsers)
                print(f"Nível de acesso do usuário {loginSubUser} alterado com sucesso!")
                del nivelAcessoSubUser
            else:
                print("Operação abortada!")


"""
@removerUsuario
"""


def removerUsuario(dicionarioUsers):
    # identificação do operador
    dadosOperador = login(dicionarioUsers)
    nivelAcessoOperador = int(dadosOperador[2])
    # coletando os dados do usuario a ser removido
    removedUser = input("digite o login do usuario que você deseja remover: ")
    if removedUser not in dicionarioUsers.keys():
        print(f"login: {removedUser} não consta no sistema")
    else:
        nivelAcessoRemovedUsr = int(dicionarioUsers[removedUser][1])
        if nivelAcessoRemovedUsr >= nivelAcessoOperador or nivelAcessoOperador < 2:
            print("Você não tem permissão suficiente para remover esse usuário")
        else:
            # confirmação
            print(f"Você quer mesmo deletar {removedUser} ?")
            print("Se sim, digite-1 caso contrário, digite-0: ")
            condicao = input()
            if condicao == "1":
                loginRUser = removedUser
                senhaRUser = dicionarioUsers[removedUser][0]
                nivelRUser = str(nivelAcessoRemovedUsr)
                # criando linha que iremos procurar no arquivo
                linhaRuser = loginRUser + "," + senhaRUser + "," + nivelRUser + "\n"
                # mexendo nos arquivos
                file = open("usuariosDescriptografados.txt", "r")
                fileDataLines = file.readlines()
                file.close()
                # deletando os dados do arquivo
                notEncryptedFile = open("usuariosDescriptografados.txt", "w")
                for line in fileDataLines:
                    if line != linhaRuser:
                        notEncryptedFile.write(line)
                notEncryptedFile.close()
                print(f"{loginRUser} removido com sucesso!")
            else:
                print(f"Operação abortada! {removedUser} não foi removido.")
