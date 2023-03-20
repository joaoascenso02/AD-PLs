import pickle as p
import struct

import sock_utils

class ListStub:

    def __init__(self, host: str, port: int) -> None:
        self.conn_sock = None
        self.host = host
        self.port = port

    def connect(self) -> None:
        # codigo para establecer uma ligacao
        # i.e., tornado self.conn_sock
        self.conn_sock = sock_utils.create_tcp_client_socket(self.host, self.port)

    def disconnect(self) -> None:
        # fecha a ligacao conn_sock
        self.conn_sock.close()

    def send_receive(self, msg: list) -> list:
        self.connect()
        msg_bytes = p.dumps(msg)
        msg_size_bytes = struct.pack("i", len(msg_bytes))

        self.conn_sock.sendall(msg_size_bytes)
        self.conn_sock.sendall(msg_bytes)

        res_size_bytes = sock_utils.receive_all(self.conn_sock, 4)
        res_size = struct.unpack("i", res_size_bytes)[0]

        res_bytes = sock_utils.receive_all(self.conn_sock, res_size)
        res = p.loads(res_bytes)

        self.disconnect()
        return res

    def append(self, element: str) -> list:
        msg = ["append"]
        msg.append(element)
        return self.send_receive(msg)

    def list(self) -> list:
        return self.send_receive(["list"])

    def clear(self) -> list:
        return self.send_receive(["clear"])
