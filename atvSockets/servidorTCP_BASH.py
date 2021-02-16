# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula  (python 3)
#

# importacao das bibliotecas
from socket import * # sockets
import subprocess

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
  while 1:
    sentence = connectionSocket.recv(1024) # recebe dados do cliente
    sentence = sentence.decode('utf-8')
    if sentence == 'exit':
      connectionSocket.send('exit'.encode('utf-8')) 
      connectionSocket.close() # encerra o socket com o cliente
      break
    output = subprocess.check_output(sentence, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
    if output != '':
      connectionSocket.send(output.encode('utf-8'))
    else:
      connectionSocket.send(" ".encode('utf-8'))
  print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

serverSocket.close() # encerra o socket do servidor
