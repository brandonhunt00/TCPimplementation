import socket

# Criando o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definindo o endereço IP e porta que o servidor irá escutar
server_socket.bind(('localhost', 12345))

# Habilitando o servidor para aceitar conexões (máximo de 1 conexão pendente)
server_socket.listen(1)
print("Servidor TCP escutando na porta 12345...")

# Aguardando por uma conexão de um cliente
conn, addr = server_socket.accept()
print(f"Conectado a {addr}")

# Recebendo dados do cliente
data = conn.recv(1024)  # Tamanho do buffer
if data:
    print("Mensagem recebida do cliente:", data.decode())

# Enviando resposta para o cliente
conn.sendall(b'Hello World!')

# Fechando a conexão
conn.close()
