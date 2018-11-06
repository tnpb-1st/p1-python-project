import funcoesComplementares as fc
import funcoesPrincipais as fp

fp.criptografarArquivo("usuariosDescriptografados.txt")
listaDescriptografada = fp.descriptografarArquivo("usuarios.txt")
dicionarioUsers = fc.criarDicionario(listaDescriptografada)
dadosUsuario = fp.login(dicionarioUsers)
fp.criptografarArquivo("usuariosDescriptografados.txt")
