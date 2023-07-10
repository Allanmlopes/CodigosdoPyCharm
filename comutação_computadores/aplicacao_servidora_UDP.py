from socket import *

servidor = "172.0.0.1"
porta=43210

obj_socket = socket(AF_INET, SOCK_DGRAM) #SOCK_DGRAM É O QUE DEFINE O PROTOCOLO UDP
obj_socket.bind((servidor, porta))
print("Servidor pronto.........:")

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem.........: ", origem)
    print("dados recebidos...: ", dados.decode())
    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)

obj_socket.close()

