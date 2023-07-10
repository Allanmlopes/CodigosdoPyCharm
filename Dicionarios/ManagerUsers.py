from Dicionarios.Funcoes_ManagerUser import *

usuarios = {}
opcao = perguntar()

# ===== Está opção esta referenciada em um dicionario chamado Funcoes_ManagerUser.py====#
#    opcao = input("O que deseja realizar?\n" +
#                  "<I> - Para inserir um usuario\n" +
#                  "<P> - Para Pesquisar um usuário\n" +
#                  "<E> - Para Excluir um usuario\n" +
#                  "<L> - Para listar um usuario: ").upper()
    # Desta forma eu nao preciso ficar digitando o valor varias vezes no meu codigo, se eu quiser realizar alguma alteração, eu vou Funcoes_ManagerUser

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao = perguntar()

# ===== Está opção esta referenciada em um dicionario chamado Funcoes_ManagerUser.py====#
#    opcao = input("O que deseja realizar?\n" +
#                  "<I> - Para inserir um usuario\n" +
#                  "<P> - Para Pesquisar um usuário\n" +
#                  "<E> - Para Excluir um usuario\n" +
#                  "<L> - Para listar um usuario: ").upper()

