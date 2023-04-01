import http.client


def main() -> None:
    try:
        while True:
            mensagem = input("Mensagem: ")

            if mensagem == "":
                continue
            elif mensagem == "EXIT":
                exit()

            comando, *argumentos = mensagem.split()

            metodo_http = None
            url_recurso = None
            corpo_pedido = None
            cabecalho_pedido = {}

            if comando == "LIST":
                metodo_http = "GET"
                url_recurso = "/lista/list"

            elif comando == "CLEAR":
                metodo_http = "POST"
                url_recurso = "/lista/clear"

            elif comando == "APPEND":
                metodo_http = "POST"
                url_recurso = "/lista/append/" + argumentos[0]

            elif comando == "CONTAINS":
                metodo_http = "GET"
                url_recurso = "/lista/contains/" + argumentos[0]

            elif comando == "UPDATE":
                metodo_http = "PUT"
                url_recurso = "/lista/update/" + argumentos[0]
                corpo_pedido = argumentos[1]
                cabecalho_pedido = {
                    'Content-Length': len(corpo_pedido.encode())}

            elif comando == "REMOVE":
                metodo_http = "DELETE"
                url_recurso = "lista/remove/" + argumentos[0]

            else:
                print("UNKNOWN-COMMAND")

            if metodo_http is not None and url_recurso is not None:
                ligacao = http.client.HTTPConnection("localhost", 8888)
                ligacao.request(metodo_http, url_recurso,
                                corpo_pedido, cabecalho_pedido)
                resposta = ligacao.getresponse()

                print(resposta.status, resposta.reason)
                print(resposta.read().decode())

                ligacao.close()

    except KeyboardInterrupt:
        print("\n Vou encerrar")
        pass

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
