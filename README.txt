Implementação TCP em Python - Hello World

Descrição:
Este projeto implementa uma comunicação básica entre cliente e servidor utilizando o protocolo TCP. O servidor escuta conexões na porta 12345 e, quando um cliente se conecta, o servidor responde com a mensagem "Hello World!".

O TCP (Transmission Control Protocol) é um protocolo orientado a conexão, que garante a entrega dos dados em ordem e sem erros. Essa implementação utiliza a biblioteca socket do Python para criar e gerenciar as conexões.

Arquivos:
- tcp_server.py: Contém a implementação do servidor TCP.
- tcp_client.py: Contém a implementação do cliente TCP.

Requisitos:
- Python 3.x
- A biblioteca padrão socket (já incluída no Python)

Como Executar:

Passo 1: Iniciar o servidor
Abra um terminal e execute o seguinte comando para iniciar o servidor:

python tcp_server.py

Você verá uma mensagem indicando que o servidor está escutando na porta 12345.

Passo 2: Iniciar o cliente
Em outro terminal, execute o seguinte comando para iniciar o cliente e se conectar ao servidor:

python tcp_client.py

O cliente enviará uma mensagem para o servidor e receberá a resposta "Hello World!" que será impressa no terminal.

Explicação do Funcionamento:

Servidor (tcp_server.py):
1. O servidor cria um socket TCP (socket.AF_INET, socket.SOCK_STREAM).
2. Ele associa o socket ao endereço localhost na porta 12345.
3. O servidor entra em modo de escuta com listen() para aceitar conexões.
4. Quando um cliente se conecta, o servidor aceita a conexão com accept().
5. O servidor lê a mensagem do cliente usando recv() e imprime no terminal.
6. Ele então responde com "Hello World!" usando sendall().
7. A conexão é fechada após o envio da mensagem.

Cliente (tcp_client.py):
1. O cliente cria um socket TCP.
2. Ele se conecta ao servidor em localhost na porta 12345 usando connect().
3. O cliente envia uma mensagem para o servidor com sendall().
4. Ele recebe a resposta do servidor e imprime a mensagem "Hello World!".
5. O cliente fecha o socket após a troca de mensagens.

Observações:
- Certifique-se de iniciar o servidor antes de rodar o cliente.
- O protocolo TCP garante que a mensagem será entregue e na ordem correta.
