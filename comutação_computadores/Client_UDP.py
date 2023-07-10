from socket import *

servidor="172.0.0.1"
porta = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor, porta))
saida = ""

while saida!="X":
    msg = input ("Sua mensagem:")
    obj_socket.sendto(msg.decode(), (servidor, porta))
    dados, origem = obj_socket.recvfrom(65535) #range maximo de portas que eu aceito a resposta 65535
    print("Resposta do servidor: ", dados.decode())
    saida = input("Digite <X> para sair").upper()

obj_socket.close()
