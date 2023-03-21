import pickle as p
import struct
import select as sel
import sys
from argparse import ArgumentParser

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


def main() -> None:

    args = parse()

    try:

        HOST = args["address"]
        PORT = args["port"]

        listen_socket = sock_utils.create_tcp_server_socket(HOST, PORT, 1)

        socket_list = [listen_socket, sys.stdin]

        lista = []
        while True:
            try:
                
                R, W, X = sel.select(socket_list, [], [])
                
                for sckt in R:
                    if sckt is sys.stdin:
                        msg = sys.stdin.readline().strip()
                        if msg == "EXIT":
                            raise SystemExit()

                    # se for a socket de escuta
                    if sckt is listen_socket:
                        conn_sock, addr = listen_socket.accept()
                        addr, port = conn_sock.getpeername()
                        print("Novo cliente ligado desde %s:%d" %(addr, port))
                        # adiciona ligacao a lista
                        socket_list.append(conn_sock)

                    # se for a socket de um cliente
                    else:
                        req_size_bytes = sock_utils.receive_all(sckt, 4)
                        req_size = struct.unpack("i", req_size_bytes)[0]

                        req_bytes = sock_utils.receive_all(sckt, req_size)
                        req = p.loads(req_bytes)

                        # se recebou dados
                        if req:

                            resp = ["Ack"]

                            if req == ["LIST"]:
                                resp = lista

                            elif req == ["CLEAR"]:
                                lista = []
                                resp = ["Lista apagada"]

                            else:
                                lista.extend(req)

                            resp_bytes = p.dumps(resp)
                            resp_size_bytes = struct.pack("i", len(resp_bytes))

                            sckt.sendall(resp_size_bytes)
                            sckt.sendall(resp_bytes)

                            print("lista = %s" % lista)
                        
                        else:
                            sckt.close()
                            socket_list.remove(sckt)
                            print("Cliente fechou a ligacao")

            except Exception as e:
                print(e)
                break

        listen_socket.close()

    except KeyboardInterrupt:
        print("\n Vou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
