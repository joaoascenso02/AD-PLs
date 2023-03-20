import pickle as p


class ListSkeleton:

    def __init__(self) -> None:
        self.servicoLista = []

    def bytesToList(self, msg_bytes: bytearray) -> list:
        return p.loads(msg_bytes)

    def listToBytes(self, msg: list) -> bytearray:
        return p.dumps(msg)

    def processMessage(self, msg_bytes: bytearray) -> bytearray:
        pedido = self.bytesToList(msg_bytes)
        resposta = []

        if pedido == None or len(pedido) == 0:
            resposta.append("INVALID MESSAGE")
        else:
            cmd, *args = pedido

            if cmd == "append" and len(pedido) > 1:
                print(self.servicoLista)
                print(args)

                self.servicoLista.extend(args)
                resposta.append("OK")

            elif cmd == "list":
                resposta = self.servicoLista

            elif cmd == "clear":
                self.servicoLista = []
                resposta.append("OK")

            elif cmd == "remove":
                pass

            elif cmd == "remove-all":
                pass

            elif cmd == "pop":
                pass

            else:
                resposta.append("INVALID MESSAGE")

        return self.listToBytes(resposta)
