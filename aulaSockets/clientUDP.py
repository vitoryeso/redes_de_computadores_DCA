from socket import *

serverName = "192.168.0.25"
serverPort = 65535

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("digite aq pra transformar em caps: ")
clientSocket.sendto(message.encode("utf-8"), (serverName, serverPort))
modifiedMessage, servAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode("utf-8"))
clientSocket.close()
