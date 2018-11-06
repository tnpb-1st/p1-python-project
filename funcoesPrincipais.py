"""
Universidade Federal de Pernambuco - UFPE
Centro de Informática
Bacharelado em Sistemas de Informação
IF968 - Programação 01
Autor: (Tomás Nascimento Pimentel Barros)(tnpb)
E-mail: (tnpb@cin.ufpe.br)
"""
import funcoesComplementares
"""
@descriptografarArquivo(nomeArquivo)
essa função tem como objetivo carregar o arquivo "usuarios.txt" e descriptografá-lo, retornando uma lista com os dados
descriptografados que servirá como parâmetro da função gerarDicionario()
"""
def descriptografarArquivo(nomeArquivo):
    listaCriptograda = funcoesComplementares.formatarArquivo(nomeArquivo)
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

def criptografarArquivo(nomeArquivo):
    listaDescriptografada = funcoesComplementares.formatarArquivo(nomeArquivo)
    def conseguirNumerosCripto():
        arquivo = open("chavePublica.txt","r")
        linha = arquivo.readline()
        arquivo.close()
        e,n = linha.split(" ")
        e,n = int(e),int(n)
        return e,n
    e,n= conseguirNumerosCripto()
    def criptografar():
        arquivo = open("usuarios.txt","w")
        for linha in listaDescriptografada:
            stringCriptografada = ""
            for caractere in linha:
                if caractere !=",":
                    y = (ord(caractere)**e)%n
                    stringCriptografada += str(y) + " "
                else:
                    stringCriptografada += ","
            arquivo.write(stringCriptografada)
            arquivo.write("\n")
        arquivo.close()
    criptografar()







