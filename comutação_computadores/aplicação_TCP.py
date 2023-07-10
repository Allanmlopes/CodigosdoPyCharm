from socket import *

servidor="127.0.0.1" #localhost
porta=43210

obj_socket = socket(AF_INET, SOCK_STREAM) #sock_stream é feito para trabalhar com TCP
obj_socket.bind((servidor, porta)) #blind é para setar qualo o endereço dos servidor,
obj_socket.listen(2) #quantidade de clientes maxima que a aplicação vai conseguir receber a conexão (escutar)


print("aguardando cliente....")

while True:
    con, cliente = obj_socket.accept() #neste accept, ele fica travado nesta linha esperando um client se conectar
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024)) #o 1024 é o tamanho do pacote, a quantidade de bytes que espero deste pacote
        print("Recebemos", msg_recebida)
        msg_recebida = b'Olah cliente'
        con.send(msg_recebida)
        break
    con.close() #fecho a conexão

#con é de conexão e o client é a identificação