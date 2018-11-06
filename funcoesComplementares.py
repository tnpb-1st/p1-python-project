"""
Universidade Federal de Pernambuco - UFPE
Centro de Informática
Bacharelado em Sistemas de Informação
IF968 - Programação 01
Autor: (Tomás Nascimento Pimentel Barros)(tnpb)
E-mail: (tnpb@cin.ufpe.br)
"""
"""
@formatarArquivo(nomeArquivo)
Pega um arquivo bruto e formata nas condições do projeto
"""
def formatarArquivo(nomeArquivo):#Pega um arquivo bruto e formata nas condições do projeto
    def abrirArquivo():
        arquivo = open(nomeArquivo,"r")
        listaLinhas = arquivo.readlines()#["login,senha,nivelAcesso\n",...,"login,senha,nivelAcesso\n"]
        arquivo.close()
        return listaLinhas

    listaLinhas = abrirArquivo()
    listaFormatada = []#["login,senha,nivelAcesso",...,"login,senha,nivelAcesso"]
    for linha in listaLinhas: #"login,senha,nivelAcesso\n"
        stringFerramenta = ""  # string temporária
        for caractere in linha:
            if caractere != "\n":
                stringFerramenta += caractere #"login,senha,nivelAcesso"
        login, senha, nivelAcesso = stringFerramenta.split(",")
        listaFormatada.append(login + ',' + senha + ',' + nivelAcesso)
    return listaFormatada

"""
@criarDicionario(listaDescriptografada)
essa função tem como objetivo criar um dicionário que servirá de parâmetro para a funcao login.
"""
def criarDicionario(listaDescriptografada):
    dicionarioUsers = {}
    for linha in listaDescriptografada:
        login, senha, nivelAcesso = linha.split(",")
        dicionarioUsers[login] = (senha, nivelAcesso)
    return dicionarioUsers