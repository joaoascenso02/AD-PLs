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
            if pedido[0] == "append" and len(pedido) > 1:
                self.servicoLista.append(pedido[1])
                resposta.append("OK")

            elif pedido[0] == "list":
                resposta.append(str(self.servicoLista))

            elif pedido[0] == "clear":
                self.servicoLista = []
                resposta.append("OK")

            elif pedido[0] == "remove":
                pass

            elif pedido[0] == "remove-all":
                pass

            elif pedido[0] == "pop":
                pass

            else:
                resposta.append("INVALID MESSAGE")

        return self.listToBytes(resposta)
