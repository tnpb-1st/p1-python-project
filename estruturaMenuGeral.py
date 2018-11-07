"""
@menuGeral() como o nome já diz, ela é o menu geral de opções para o usuário
"""
import funcoesComplementares as fc
import funcoesPrincipais as fp


def menuGeral():
    '#condicao para o programa rodar'
    menuRodando = True
    while menuRodando:
        fp.criptografarArquivo("usuariosDescriptografados.txt")
        # variaveis globais
        listaDescriptografada = fp.descriptografarArquivo("usuarios.txt")
        dicionarioUsers = fc.criarDicionario(listaDescriptografada)
        mensagemInput = """\
        --------------------------------
        Digite:
        1 - Realizar Login
        2 - Cadastrar-se
        3 - Alteração de Nível de Usuário
        4 - Remover Usuário
        0 - Sair
        --------------------------------
        """
        print(mensagemInput)
        opcaoUser = int(input())
        # se o usuario quiser realizar o login
        if opcaoUser == 1:
            fp.login(dicionarioUsers)
        # se um novo usuario quiser se cadastrar
        elif opcaoUser == 2:
            fp.cadastrarUsuario(dicionarioUsers)
        # se um usuario de hierarquia superior quiser alterar um de hierarquia
        # inferior
        elif opcaoUser == 3:
            fp.alterarNivelUsuario(dicionarioUsers)
        # remover um usuário que não tenha nível de gerência
        elif opcaoUser == 4:
            fp.removerUsuario(dicionarioUsers)
        # sair do programa
        elif opcaoUser == 0:
            menuRodando = False
        else:
            opcoes = (0, 1, 2, 3)
            while opcaoUser not in opcoes:
                print("Escolha inválida de menu, escolha uma das opções disponíveis")
                opcaoUser = int(input())
        fp.criptografarArquivo("usuariosDescriptografados.txt")
