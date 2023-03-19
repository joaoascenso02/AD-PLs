class ListStub:

    def __init__(self, host: str, port: int) -> None:
        self.conn_sock = None
        self.host = host
        self.port = port

    def connect(self, host, port):
        # codigo para establecer uma ligacao
        # i.e., tornado self.conn_sock
        pass

    def disconnect(self):
        # fecha a ligacao conn_sock
        pass

    # Metodos tradicionais de um objeto do tipo lista
    def append(self, element):
        pass

    def list(self):
        pass

    def clear(self):
        pass

    # Outros possiveis metodos
