from socket import *
import threading
import time

def send(sock):
    while True:
        sendData = input(">>>")
        sock.send(sendData.encode('utf-8'))
        if sendData == 'Q':
            clientSock.close()
            print('대화종료\n')
        
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('\n상대방:', recvData.decode('utf-8'))
        
clientSock = socket(AF_INET, SOCK_STREAM)
connectionSock, addr = clientSock.connect(('192.168.55.206', 8081))

print('접속완료')
print(addr)

sender = threading.Thread(target = send, args = (clientSock, ))
receiver = threading.Thread(target = receive, args = (clientSock, ))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
