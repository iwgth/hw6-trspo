import socket

# адреса та порт сервера
server_address = ('localhost', 12345)
# створення сокету та очікування з'єднання 2
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)
print("очікуємо підключення...")
client_socket, client_address = server_socket.accept()
print(f"підключення встановлено з {client_address}")

# отримали та відправили повідомлення
for i in range(1, 101):
    # отримуємо повідомлення від клієнта
    message_length_bytes = client_socket.recv(4)
    message_length = int.from_bytes(message_length_bytes, byteorder='big')
    message = client_socket.recv(message_length)
    decoded_message = message.decode()
    print(f"отримано від клієнта: {decoded_message}")
    # відправляємо відповідь клієнту
    response = f"отримана відповідь від сервера на повідомлення номер {i}".encode()
    response_length = len(response).to_bytes(4, byteorder='big')
    client_socket.send(response_length + response)

client_socket.close()
server_socket.close()
