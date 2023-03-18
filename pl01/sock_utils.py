import socket as s


def create_tcp_server_socket(address: str, port: int, queue_size: int) -> s.socket:
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    sock.bind((address, port))
    sock.listen(queue_size)
    return sock


def create_tcp_client_socket(address: str, port: int) -> s.socket:
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect((address, port))
    return sock


def receive_all(socket: s.socket, length: int) -> bytearray:
    data = bytearray()

    while len(data) < length:
        packet = socket.recv(length - len(data))

        if len(packet) == 0:
            break

        data.extend(packet)

    return data
