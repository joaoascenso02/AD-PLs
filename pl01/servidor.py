import socket as s
import sys
from argparse import ArgumentParser


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


def main() -> None:

    args = parse()

    try:

        HOST = args["address"]
        PORT = args["port"]

        sock = s.socket(s.AF_INET, s.SOCK_STREAM)

        # para prevenir que a socket se ligue mesmo que o processo
        # do do protocolo tcp do servidor anterior ainda nao tenha encerrado
        sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

        sock.bind((HOST, PORT))

        # quantos clientes se podem ligar
        sock.listen(1)

        while True:
            try:
                (conn_sock, (addr, port)) = sock.accept()
                print("ligado a %s, no porto %s" % (addr, port))
                msg = conn_sock.recv(1024)

                reposta = msg.decode()

                print("recebi %s" % reposta)

                conn_sock.sendall(reposta.encode())
                conn_sock.close()

            except Exception as e:
                print(e)
                break

        sock.close()

    except KeyboardInterrupt:
        print("\nVou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
