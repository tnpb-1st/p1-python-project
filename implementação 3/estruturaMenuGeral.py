import funcoesComplementares as fc
import funcoesPrincipais as fp
import datetime
"""
Universidade Federal de Pernambuco - UFPE
Centro de Informática
Bacharelado em Sistemas de Informação
IF968 - Programação 01
Autor: (Tomás Nascimento Pimentel Barros)(tnpb)
E-mail: (tnpb@cin.ufpe.br)
"""


def menuGeral():
    """
    @menuGeral() como o nome já diz, ela é o menu geral de opções para o usuário e chama todas as funções essenciais
    ao código
    """
    # var
    listaDescriptografadaUser = fp.descriptografarArquivo("usuarios.txt", "private/usuariosDescriptografados.txt")
    dicionarioUsers = fc.criarDicionario(listaDescriptografadaUser)
    listaDescriptografadaElem = fp.descriptografarArquivo("elementos.txt", "private/elementosDescriptografados.txt")
    # login do usuário e seus dados
    dadosUsuario = fp.login(dicionarioUsers)
    # condicao para o programa rodar
    if type(dadosUsuario) != type(None):
        loginUser = dadosUsuario[0]
        nivelAcessoUser = dadosUsuario[2]
        menuRodando = True
    else:
        menuRodando = False
    # sicronização inicial
    fp.criptografarArquivo("private/usuariosDescriptografados.txt")
    fp.criptografarElementos("private/elementosDescriptografados.txt")
    while menuRodando:
        # variaveis globais
        listaDescriptografadaUser = fp.descriptografarArquivo("usuarios.txt", "private/usuariosDescriptografados.txt")
        listaDescriptografadaElem = fp.descriptografarArquivo("elementos.txt", "private/elementosDescriptografados.txt")
        dicionarioElem = fc.criarDicionarioElem(listaDescriptografadaElem)
        dicionarioUsers = fc.criarDicionario(listaDescriptografadaUser)
        fp.ordenarClientes(dicionarioElem)
        fc.mostruarioElementos(listaDescriptografadaElem)
        mensagemInput = """\
        --------------------------------
        Digite:
        1 - Cadastrar novo usuário
        2 - Alteração de nível de usuário
        3 - Remover usuário
        4 - Cadastrar cliente
        5 - Remover cliente
        6 - Buscar cliente
        7 - Atualizar dados do cliente
        8 - Mostrar log de ações por data ou por usuário
        0 - Sair
        --------------------------------
        """
        print(mensagemInput)
        opcaoUser = int(input())
        # cadastro de novo usuário
        if opcaoUser == 1:
            fp.cadastrarUsuario(dicionarioUsers, nivelAcessoUser)
            acao = loginUser + "; usou a função cadastrarUsuario()"
            time = str(datetime.datetime.now())
        # se um usuario de hierarquia superior quiser alterar um de hierarquia
        # inferior
        elif opcaoUser == 2:
            fp.alterarNivelUsuario(dicionarioUsers, nivelAcessoUser)
            acao = loginUser + "; usou a função alterarNivelUsuario()"
            time = str(datetime.datetime.now())
        # remover um usuário que não tenha nível de gerência
        elif opcaoUser == 3:
            fp.removerUsuario(dicionarioUsers, nivelAcessoUser)
            acao = loginUser + "; usou a função usuarioRemovido()"
            time = str(datetime.datetime.now())
        # adicionar um cliente ao sistema da padaria
        elif opcaoUser == 4:
            fp.cadastrarCliente(dicionarioElem)
            acao = loginUser + "; usou a função cadastrarCliente()"
            time = str(datetime.datetime.now())
        # remover um cliente do sistema da padaria
        elif opcaoUser == 5:
            fp.removerCliente(dicionarioElem, nivelAcessoUser)
            acao = loginUser + "; usou a função removerCliente()"
            time = str(datetime.datetime.now())
        # buscar dados de um cliente
        elif opcaoUser == 6:
            fp.buscarCliente(dicionarioElem)
            acao = loginUser + "; usou a função buscarCliente()"
            time = str(datetime.datetime.now())
        # alterar atributos de um cliente
        elif opcaoUser == 7:
            fp.alterarDadosCliente(dicionarioElem, nivelAcessoUser)
            acao = loginUser + "; usou a função alterarDadosCliente()"
            time = str(datetime.datetime.now())
        # buscar log das ações por data ou por usuário
        elif opcaoUser == 8:
            fp.buscarLogUsuario()
            acao = loginUser + "; usou a função buscarLogUsuario()"
            time = str(datetime.datetime.now())
        # sair do programa
        elif opcaoUser == 0:
            acao = loginUser + "; saiu do sistema "
            time = str(datetime.datetime.now())
            menuRodando = False
        else:
            opcoes = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
            while opcaoUser not in opcoes:
                print("Escolha inválida de menu, escolha uma das opções disponíveis")
                opcaoUser = int(input())
        # atualização dos arquivos criptografados e deixar em branco os arquivos com as informações
        # descriptografadas
        fp.criptografarArquivo("private/usuariosDescriptografados.txt")
        fp.criptografarElementos("private/elementosDescriptografados.txt")
        fp.criarLogUsuario(acao, time)
        fc.eraseFiles()
