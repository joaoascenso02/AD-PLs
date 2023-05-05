import sys
import socket as s
from argparse import ArgumentParser
import traceback
import ssl


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

        context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname = True
        context.load_verify_locations(cafile="root.pem")
        # autenticacao mutua
        context.load_cert_chain(certfile="cli.crt", keyfile="cli.key")

        while True:
            try:
                msg = input("Mensagem: ")

                if msg == "EXIT":
                    exit()

                sock = s.socket(s.AF_INET, s.SOCK_STREAM)
                sock.connect((HOST, PORT))

                sslsock = context.wrap_socket(sock, server_hostname=HOST)

                sslsock.sendall(msg.encode())
                resposta = sslsock.recv(1024)

                print(f"Recebi: {resposta.decode()}")

            except:
                traceback.print_exc()
                break

        sslsock.close()

    except:
        traceback.print_exc()


if __name__ == "__main__":
    main()
