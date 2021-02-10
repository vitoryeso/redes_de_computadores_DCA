# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula  (python 3)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

errorMsg = "ERROR: " # mensagem de erro

while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  if sentence[:4] == "open":
    try:
      arq = open(sentence[5:])
      clientResponse = arq.read()
      print ("Cliente :{} enviou: {}, enviando o conteudo do arquivo: {}".format(addr, sentence, sentence[5:]))
    except:
      clientResponse = errorMsg + "File not found!" 
      print ("Cliente :{} enviou: {}, enviando a mensagem de erro: {}".format(addr, sentence, clientResponse))

  else:
      clientResponse = errorMsg + "wrong command!"
      print ("Cliente :{} enviou: {}, enviando a mensagem de erro: {}".format(addr, sentence, clientResponse))

  connectionSocket.send(clientResponse.encode('utf-8')) # envia para o cliente o texto transformado
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor
