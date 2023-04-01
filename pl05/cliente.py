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
                pass

            elif comando == "UPDATE":
                pass

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
