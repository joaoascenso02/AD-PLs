import pickle as p
import struct
from argparse import ArgumentParser
import socketserver

import sock_utils


def parse() -> dict:
    parser = ArgumentParser(
        description="Servidor"
    )

    parser.add_argument(
        "address",
        help="ip ou hostname do servidor",
        default="localhost"
    )

    parser.add_argument(
        "port",
        help="porto tcp onde o servidor recebe pedidos de ligacao",
        type=int,
        default=9999
    )

    args = parser.parse_args().__dict__

    return args

class MyHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        
        global lista
        # self.request e a socket ligada ao cliente
        print("ligado a ", self.client_address)

        req_size_bytes = sock_utils.receive_all(self.request, 4)
        req_size = struct.unpack("i", req_size_bytes)[0]

        req_bytes = sock_utils.receive_all(self.request, req_size)
        req = p.loads(req_bytes)

        print(req)

        resp = ["Ack"]

        if req == ["LIST"]:
            resp = lista

        elif req == ["CLEAR"]:
            lista = []
            resp = ["Lista apagada"]

        else:
            lista.extend(req)

        resp_bytes = p.dumps(resp)
        print(resp)
        print(resp_bytes)
        resp_size_bytes = struct.pack("i", len(resp_bytes))
        print(resp_size_bytes)

        self.request.sendall(resp_size_bytes)
        self.request.sendall(resp_bytes)

        print("lista = %s" % lista)


def main() -> None:

    args = parse()

    try:
        HOST = args["address"]
        PORT = args["port"]

        server = socketserver.ThreadingTCPServer((HOST, PORT), MyHandler)
        server.serve_forever(2.0)

    except KeyboardInterrupt:
        print("\n Vou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    lista = []
    main()
