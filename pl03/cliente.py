import sys
import socket as s
from argparse import ArgumentParser

import sock_utils
from stub import ListStub

def parse() -> dict:
    parser = ArgumentParser(
        description="Cliente"
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


def main() -> None:

    args = parse()

    try:

        HOST = args["address"]
        PORT = args["port"]

        stub = ListStub()

        while True:

            try:
                msg = input("Mensagem: ")
                if msg == "EXIT":
                    exit()

                sock = sock_utils.create_tcp_client_socket()

                # send receive: change to use pickle
                sock.sendall(msg.encode())
                resposta = sock.recv(1024)

                print("Recebi: %s" % resposta.decode())
                sock.close()

            except Exception as e:
                print(e)

    except KeyboardInterrupt:
        print("\nVou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
