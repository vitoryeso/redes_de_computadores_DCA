# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets TCP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula (python 3)
#

# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

print('Terminal remoto iniciado. digite exit para sair.')

cmd = input('servidor:{}$ '.format(serverName))

while True:
	clientSocket.send(cmd.encode('utf-8')) # envia o comando para o servidor
	output = clientSocket.recv(1024).decode('utf-8') # recebe do servidor a resposta
	if output == 'exit':
		break
	elif output == '':
		print('')
	else:
		print(output)
	cmd = input('servidor:{}$ '.format(serverName))

clientSocket.close() # encerramento o socket do cliente

