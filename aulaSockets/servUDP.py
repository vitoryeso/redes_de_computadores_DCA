from socket import *

serverPort = 65535
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(("", serverPort))

print("servidor ON rapazeadinha hehe")
while True:
    message, clientAddress = serverSocket.recvfrom(2048) # clientAddress eh o endereco e a porta
    modifiedMessage = message.decode("utf-8")
    serverSocket.sendto(modifiedMessage.upper().encode("utf-8"), clientAddress)
