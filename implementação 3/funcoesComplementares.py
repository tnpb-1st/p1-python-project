"""
Universidade Federal de Pernambuco - UFPE
Centro de Informática
Bacharelado em Sistemas de Informação
IF968 - Programação 01
Autor: (Tomás Nascimento Pimentel Barros)(tnpb)
E-mail: (tnpb@cin.ufpe.br)
"""


def formatarArquivo(nomeArquivo):  # Pega um arquivo bruto e formata nas condições do projeto
    """
    @formatarArquivo(nomeArquivo)
    Pega um arquivo bruto e formata nas condições do projeto
    """
    def abrirArquivo():
        arquivo = open(nomeArquivo, "r")
        listaLinhas = arquivo.readlines()  # ["login,senha,nivelAcesso\n",...,"login,senha,nivelAcesso\n"]
        arquivo.close()
        return listaLinhas

    listaLinhas = abrirArquivo()
    listaFormatada = []  # ["login,senha,nivelAcesso",...,"login,senha,nivelAcesso"]
    for linha in listaLinhas:  # "login,senha,nivelAcesso\n"
        stringFerramenta = ""  # string temporária
        for caractere in linha:
            if caractere != "\n":
                stringFerramenta += caractere  # "login,senha,nivelAcesso"
        login, senha, nivelAcesso = stringFerramenta.split(",")
        listaFormatada.append(login + ',' + senha + ',' + nivelAcesso)
    return listaFormatada


def criarDicionario(listaDescriptografada):
    """
    @criarDicionario(listaDescriptografada)
    essa função tem como objetivo criar um dicionário que servirá de parâmetro para a funcao login.
    """
    dicionarioUsers = {}
    for linha in listaDescriptografada:
        linhaString = ""
        for caractere in linha:
            if caractere != "\n":
                linhaString += caractere
        login, senha, nivelAcesso = linhaString.split(",")
        dicionarioUsers[login] = (senha, nivelAcesso)
    return dicionarioUsers


def criarDicionarioElem(listaDescriptografada):
    """
    @criarDicionarioElem cria um dicionario dos clientes, tendo o CPF como chave e (primeiro nome,ultimo nome, email,cep, gasto na padaria) como tupla de atributos
    """
    dicionarioElem = {}
    for linha in listaDescriptografada:
        linhaString = ""
        for caractere in linha:
            if caractere != "\n":
                linhaString += caractere
        cpf, firstName, lastName, email, cep, gastosPadaria = linhaString.split(",")
        dicionarioElem[cpf] = (firstName, lastName, email, cep, gastosPadaria)
    return dicionarioElem


def modificarArquivo(dicionarioUsers):
    """
    @modificarArquivo() função auxiliar minha, nem lembro se usei no código final
    """

    # estocando os dados do arquivo
    originalFile = open("private/usuariosDescriptografados.txt", "r")
    dataFileLines1 = originalFile.readlines()
    originalFile.close()
    # mudando os dados do arquivo
    newFile = open("private/usuariosDescriptografados.txt", "w")
    linhaProcurada = "insira a linha aqui"
    linhaSubstita = "insira a nova linha aqui"
    for line in dataFileLines1:
        if line != linhaProcurada:
            newFile.write(line)
        else:
            newFile.write(linhaSubstita)
    newFile.close()


def eraseFiles():
    """
    @eraseFiles essa função auxiliar apaga informações privadas dos usuários e dos elementos, que ficam respectivamente
    armazenadas nos arquivos usuariosDescriptografados.txt e elementosDescriptografados.txt dentro da pasta private.
    Esses arquivos são vitais para o funcionamento de todo o código, no entanto eles só armazenam as informações enquanto
    o programa está sendo rodado, uma vez que sempre que o usuário sai do programa, a função eraseFiles() apaga o conteúdo
    desses arquivos.

    ATENÇÃO caso queira ver o funcionamento desses arquivos mencionados, basta comentar a função eraseFiles() na linha
    116 do arquivo estruturaMenuGeral.py
    """
    file1 = open("private/usuariosDescriptografados.txt", "w")
    file1.close()
    file2 = open("private/elementosDescriptografados.txt", "w")
    file2.close()


def formatarELementos(elementosDescriptografados):
    """
    @formatarElementos função auxiliar
    """
    def abrirArquivo():
        arquivo = open(elementosDescriptografados, "r")
        listaLinhas = arquivo.readlines()
        arquivo.close()
        return listaLinhas

    listaLinhas = abrirArquivo()
    listaFormatada = []
    for linha in listaLinhas:
        stringFerramenta = ""
        for caractere in linha:
            if caractere != "\n":
                stringFerramenta += caractere
        cpf, fn, ln, email, cep, money = stringFerramenta.split(',')
        listaFormatada.append(cpf + ',' + fn + ',' + ln + ',' + email + ',' + cep + ',' + money)
    return listaFormatada


def mostruarioElementos(listaDescriptografada):
    """
    @mostruarioElementos() cria o arquivo com todas as informações dos clientes de maneira organizada
    no arquivo mostruarioElementos.txt conforme requisitado no projeto
    """
    listaFormatada = []
    for string in listaDescriptografada:
        stringTemp = ""
        for caractere in string:
            if caractere != "\n":
                stringTemp += caractere
        listaFormatada.append(stringTemp)

    tamanho = len(listaFormatada)
    file = open("impressaoElementos.txt", "w")
    for indice in range(tamanho):
        cpf, fn, ln, email, cep, money = listaFormatada[indice].split(',')
        # output
        output = f"""\
        ---------------------------------------------
        CPF: {cpf}
        PRIMEIRO NOME: {fn}
        ÚLTIMO NOME: {ln}
        E-MAIL: {email}
        CEP: {cep}
        GASTO NA PADARIA: R${money}
        ---------------------------------------------
        """
        file.write(output)
        file.write('\n')
    file.close()
