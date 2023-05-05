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

        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

        sock.bind((HOST, PORT))
        sock.listen(1)

        context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
        # context.verify_mode = ssl.CERT_NONE

        # autenticacao mutua
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile="root.pem")

        context.load_cert_chain(certfile="serv.crt", keyfile="serv.key")

        lista = []

        while True:
            try:
                (conn_sock, addr) = sock.accept()
                sslsock = context.wrap_socket(conn_sock, server_side=True)

                tmp = sslsock.recv(1024)
                msg = tmp.decode()
                resp = "ACK"

                if msg == "LIST":
                    resp = str(lista)

                elif msg == "CLEAR":
                    lista = []
                    resp = "Lista apagada"

                else:
                    lista.append(msg)

                sslsock.sendall(resp.encode())

                print(f"List = {lista}")
                sslsock.close()

            except:
                traceback.print_exc()
                break

        sock.close()

    except:
        traceback.print_exc()


if __name__ == "__main__":
    main()
