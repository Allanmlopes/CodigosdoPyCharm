from socket import *

servidor="127.0.0.1"
porta=43210

msg = bytes(input("Digite algo: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM) #AF_INET = vou me identificar por IP ou hostiname, e o SOCK_STREAM =  estou deficindo qual o protocolo (no caso TCP)
obj_socket.connect((servidor, porta))
obj_socket.send(msg)
resposta=obj_socket.recv(1024)
print("Recebemos:", resposta)
obj_socket.close()

