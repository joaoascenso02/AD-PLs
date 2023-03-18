import socket as s
import sys

from argparse import ArgumentParser


def parse():
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


def main():

    args = parse()

    try:

        HOST = args["address"]
        PORT = args["port"]

        while True:
            mensagem = input("> ")

            if not mensagem:
                continue
            elif mensagem == "EXIT":
                break

            sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            sock.connect((HOST, PORT))

            sock.sendall(mensagem.encode())

            resposta = sock.recv(1024)

            print("Recebi %s" % resposta.decode())

            sock.close()

    except KeyboardInterrupt:
        print("\nVou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
