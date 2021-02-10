# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets UDP modificado para receber texto minusculo do cliente enviar resposta em maiuscula (python 3)
#

# importacao das bibliotecas
from socket import * # sockets
from time import ctime

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
    if message == "data" or "DATA":
        dataMessage = str(ctime())
        print("Cliente :{} enviou :{}. enviando para ele a data :{}".format(clientAddress, message, dataMessage))
    else:
        dataMessage = "ERROR (pedido incorreto)"
        print("Cliente :{} enviou :{}. enviando para ele a mensagem de erro :{}".format(clientAddress, message, dataMessage))

    serverSocket.sendto(dataMessage.encode('utf-8'), clientAddress) 
# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor
