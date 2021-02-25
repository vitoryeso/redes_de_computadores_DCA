# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTORES: VITOR YESO FIDELIS FREITAS
#          IGOR FERREIRA DE PAIVA
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# funcao auxiliar para gerar respostas http
def http_response(status_code, html_page=None):
    if status_code == 200:
        if html_page: return "HTTP/1.1 200 OK\r\n\r\n"+html_page
        else:
            return "HTTP/1.1 200 OK\r\n\r\nHello, World!\r\n"
    elif status_code == 400:
        return "HTTP/1.1 400 Bad Request\r\n\r\n<html>\n\t<head></head>\n\t<body>\n\t\t<h1>400 Bad Request</h1>\n\t</body>\n</html>\r\n"
    elif status_code == 404:
        return "HTTP/1.1 404 Not Found\r\n\r\n<html>\n\t<head></head>\n\t<body>\n\t\t<h1>404 Not Found</h1>\n\t</body>\n</html>\r\n"
    else: return ""
        
        
# importacao das bibliotecas
import socket

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()

    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)

    request_str = request.decode('utf-8')

    try:
        # pegando somente o arquivo solicitado e o metodo HTTP
        method_name, file_name = request_str.split(' ')[0:2]
        check_msg = True
    except:
        response = http_response(400)
        check_msg = False

    if check_msg:
        if method_name != 'GET': response = http_response(400)

        elif file_name == '/': 
            page = open('./index.html').read()
            response = http_response(200, page)
        else:
            try:
                page = open('.' + file_name, 'r').read()
                response = http_response(200, page)
            except:
                response = http_response(404)

    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    client_connection.send(response.encode('utf-8'))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()
