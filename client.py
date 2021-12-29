import socket

# permitindo a utilização do servidor af_inet utilizar protocolo tcp ip 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(('localhost', 8888))

finish = False
print('Write "finish chat" for terminate this chat')

while not finish:
    client.send(input("input yor menssage: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'finish chat':
        finish = True

    else:
        print(msg)

client.close()