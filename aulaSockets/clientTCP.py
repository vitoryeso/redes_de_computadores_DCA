from socket import *;

serverIP = "192.168.0.25";
serverPort = 65535;

clientSocket = socket(AF_INET, SOCK_STREAM);
clientSocket.connect((serverIP, serverPort)); # aqui ativa o accept do servidor

sentence = input("digite um texto pra ser convertido pra caps: ");
clientSocket.send(str.encode(sentence));
modifiedSentence = clientSocket.recv(1024).decode("utf-8"); # recebendo 1024 bytes do servidor

print("resposta do servidor: ");
print(modifiedSentence);

clientSocket.close();
