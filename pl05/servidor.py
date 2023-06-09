import http.server
import socketserver
import json

PORT = 8888
HOST = "localhost"

list = []


class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):

    def _set_headers(self, http_code=200) -> None:
        self.send_response(http_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self) -> None:
        global list

        path_segments = [ps for ps in self.path.split("/") if ps != ""]

        if path_segments[0] == "lista":
            if path_segments[1] == "list":
                self._set_headers(200)
                self.wfile.write(json.dumps(list).encode())

            elif path_segments[1] == "contains":
                print(path_segments)
                print(list)
                if path_segments[2] in list:
                    self._set_headers(200)
                    self.wfile.write(path_segments[2].encode())

                else:
                    self._set_headers(404)

            else:
                self._set_headers(404)

        else:
            self._set_headers(404)

    def do_POST(self) -> None:
        global list

        path_segments = [ps for ps in self.path.split("/") if ps != ""]

        if path_segments[0] == "lista":
            if path_segments[1] == "clear":
                list.clear()
                self._set_headers(204)

            elif path_segments[1] == "append":
                list.append(path_segments[2])
                self._set_headers(201)

            else:
                self._set_headers(404)

        else:
            self._set_headers(404)

    def do_PUT(self) -> None:
        global list

        path_segments = [ps for ps in self.path.split("/") if ps != ""]

        if path_segments[0] == "lista":
            if path_segments[1] == "update":
                content_length = int(self.headers['Content-Length'])
                new_word = self.rfile.read(content_length).decode()

                if content_length != 0:
                    if path_segments[2] in list:
                        index = list.index(path_segments[2])
                        list.pop(index)
                        list.insert(index, new_word)
                        self._set_headers(200)

                    else:
                        list.append(path_segments[2])
                        self._set_headers(201)

                else:
                    self._set_headers(400)

            else:
                self._set_headers(404)

        else:
            self._set_headers(404)

    def do_DELETE(self) -> None:
        global list

        path_segments = [ps for ps in self.path.split("/") if ps != ""]

        if path_segments[0] == "lista":
            if path_segments[1] == "remove":
                if path_segments[2] in list:
                    list.remove(path_segments[2])
                    self._set_headers(200)

                else:
                    self._set_headers(404)

            else:
                self._set_headers(404)

        else:
            self._set_headers(404)


def main() -> None:
    HTTP_server = socketserver.TCPServer((HOST, PORT), MyHTTPHandler, True)
    HTTP_server.allow_reuse_address = True

    try:
        HTTP_server.serve_forever(2.0)

    except KeyboardInterrupt:
        print("\n Vou encerrar")
        pass

    except Exception as e:
        print(e)
        pass

    HTTP_server.shutdown()


if __name__ == "__main__":
    main()
