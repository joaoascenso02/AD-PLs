class ListSkeleton:

    def __init__(self):
        self.servicoLista = [];

    def processMessage(self, msg_bytes):
        pedido = bytesToList(msg_bytes)

        resposta = [];

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

            else:
                resposta.append("INVALID MESSAGE")

        return listToBytes(resposta)
    
    # fim do metodo processMessage

    # outros metodos possiveis

    def bytesToList(self, msg_bytes):
        pass

    def listToBytes(self, msg):
        pass