from argparse import ArgumentParser

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

        stub = ListStub(HOST, PORT)

        while True:
            try:
                msg = input("Mensagem: ")
                
                if msg == "":
                    continue
                elif msg == "EXIT":
                    exit()

                cmd, *args = msg.split()
                res = []
                if cmd == "list":
                    res = stub.list()

                elif cmd == "clear":
                    res = stub.clear()

                elif cmd == "remove":
                    pass

                elif cmd == "remove-all":
                    pass

                elif cmd == "pop":
                    pass

                else:
                    res = stub.append(msg)

                print("Recebi: %s" % res)

            except Exception as e:
                print(e)

    except KeyboardInterrupt:
        print("\nVou encerrar!")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
