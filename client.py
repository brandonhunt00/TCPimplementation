import socket

# Criando o socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect(('localhost', 12345))

# Enviando dados para o servidor
client_socket.sendall(b'Hello from client')

# Recebendo resposta do servidor
data = client_socket.recv(1024)
print("Mensagem recebida do servidor:", data.decode())

# Fechando o socket
client_socket.close()
