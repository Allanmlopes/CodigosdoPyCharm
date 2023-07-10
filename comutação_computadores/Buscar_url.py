import socket

resp="S"
while(resp=="S"):
    url=input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    print("O IP referente a url informada é: ", ip)
    resp=input("Digite <s> para continuar :").upper()

#a biblioteca do socket é muito importante para poder fazer uma distribuição das nossas aplicações para comunicar um computador com o outro.
#para fazer uma aplicação distribuida tem que utilizar SOCKET. tanto numa rede local quanto numa rede global como a internet
