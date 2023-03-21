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

        sock = sock_utils.create_tcp_client_socket(HOST, PORT)

        while True:
            try:
                msg = list()
                msg.append(str(input("Mensagem: ")))

                if msg == [""]:
                    continue
                elif msg == ["EXIT"]:
                    break

                msg_bytes = p.dumps(msg)
                msg_size_bytes = struct.pack("i", len(msg_bytes))

                sock.sendall(msg_size_bytes)
                sock.sendall(msg_bytes)

                resp_size_bytes = sock_utils.receive_all(sock, 4)
                print(resp_size_bytes)
                resp_size = struct.unpack("i", resp_size_bytes)[0]

                resp_bytes = sock_utils.receive_all(sock, resp_size)
                m = p.loads(resp_bytes)

                print("Recebi: %s" % m)

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
