from socket import *;

serverPort = 65535;
serverSocket = socket(AF_INET, SOCK_STREAM);
serverSocket.bind(("", serverPort));
serverSocket.listen(1);

print("Servidor ON rapaziadinha");
while True:
    connectionSocket, addr = serverSocket.accept();
    sentence = connectionSocket.recv(1024); # recebendo 1024 bytes
    capitalizedSentence = sentence.decode("utf-8").upper();
    connectionSocket.send(capitalizedSentence.encode("utf-8"));
    connectionSocket.close()


