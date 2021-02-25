from socket import *

serverName = 'localHost'
serverPort = 60000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

cmd = input("digite verme: ")

while True:
	clientSocket.send(cmd.encode('utf-8'))
	output = clientSocket.recv(1024).decode('utf-8')

	print(output)
	cmd = input("$$: ")

