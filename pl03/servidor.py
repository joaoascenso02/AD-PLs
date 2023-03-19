import struct
from argparse import ArgumentParser

import sock_utils
from skeleton import ListSkeleton


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

        sock = sock_utils.create_tcp_server_socket(HOST, PORT, 1)

        skeleton = ListSkeleton()

        while True:
            try:

                (conn_sock, addr) = sock.accept()

                req_size_bytes = sock_utils.receive_all(conn_sock, 4)
                req_size = struct.unpack("i", req_size_bytes)[0]

                req_bytes = sock_utils.receive_all(conn_sock, req_size)
                
                resp_bytes = skeleton.processMessage(req_bytes)

                resp_size_bytes = struct.pack("i", len(resp_bytes))

                conn_sock.sendall(resp_size_bytes)
                conn_sock.sendall(resp_bytes)

                conn_sock.close()

            except Exception as e:
                print(e)
                break

        sock.close()

    except KeyboardInterrupt:
        print("\n Vou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
