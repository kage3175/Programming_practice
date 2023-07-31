from socket import *
import threading
import time

def send(sock):
    while True:
        sendData = input(">>>")
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print("상대방:", recvData.decode('utf-8'))

port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print(f'{port}번 포트로 접속 대기중...')

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target = send, args = (connectionSock, ))
receiver = threading.Thread(target = receive, args = (connectionSock, ))

sender.start()
receiver.start()

cnt=0
while True:
    time.sleep(1)
    cnt+=1
    msg = "Host notifies " + str(cnt) + " seconds has gone\n"
    connectionSock.send(msg.encode('utf-8'))
    pass