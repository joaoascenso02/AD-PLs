import pickle as p
import struct
from argparse import ArgumentParser

import sock_utils


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

        while True:

            try:

                msg = list()
                msg.append(str(input("Mensagem: ")))

                if msg == [""]:
                    continue
                elif msg == ["EXIT"]:
                    break

                conn_sock = sock_utils.create_tcp_client_socket(HOST, PORT)

                msg_bytes = p.dumps(msg)
                msg_size_bytes = struct.pack("i", len(msg_bytes))

                conn_sock.sendall(msg_size_bytes)
                conn_sock.sendall(msg_bytes)

                resp_size_bytes = conn_sock.recv(4)
                resp_size = struct.unpack("i", resp_size_bytes)[0]

                resp_bytes = conn_sock.recv(resp_size)

                m = p.loads(resp_bytes)

                print("Recebi: %s" % m)
                conn_sock.close()

            except Exception as e:
                print(e)

    except KeyboardInterrupt:
        print("\nVou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
