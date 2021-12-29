import socket

# permitindo a utilização do servidor af_inet utilizar protocolo tcp ip 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))

server.listen()

client, adress = server.accept()

finish = False

while not finish:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'finish chat':
        finish = True

    else:
        print(msg)
    
    client.send(input('input yor menssage: '))

client.close()
server.close()