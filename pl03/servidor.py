import sys
import socket as s
from argparse import ArgumentParser

import sock_utils


def parse():
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


def main():

    args = parse()

    try:

        HOST = args["address"]
        PORT = args["port"]

        sock = sock_utils.create_tcp_server_socket(HOST, PORT, 1)

        list = []
        while True:
            try:

                
                (conn_sock, addr) = sock.accept()
                msg = conn_sock.recv(1024)
                
                
                resp = "Ack"

                if msg.decode() == "LIST":
                    resp = str(list)

                elif msg.decode() == "CLEAR":
                    list = []
                    resp = "Lista apagada"

                else:
                    list.append(msg.decode())

                conn_sock.sendall(resp.encode())

                print("list= %s" % list)
                conn_sock.close()

            except:
                print("Socket fechado!")
                conn_sock.close()

    except KeyboardInterrupt:
        print("\n Vou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
