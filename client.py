import socket

# адреса та порт сервера
server_address = ('localhost', 12345)
# створення сокету та з'єднання з сервером 2
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# відправка та отримання повідомлень
for i in range(1, 101):
    message = f"отримане повідомлення від клієнта {i}".encode()
    message_length = len(message).to_bytes(4, byteorder='big')
    client_socket.send(message_length + message)

    # отримуємо відповіді від сервера
    response_length_bytes = client_socket.recv(4)
    response_length = int.from_bytes(response_length_bytes, byteorder='big')
    response = client_socket.recv(response_length)
    decoded_response = response.decode()
    print(f"отримана відповідь від сервера: {decoded_response}")

client_socket.close()
